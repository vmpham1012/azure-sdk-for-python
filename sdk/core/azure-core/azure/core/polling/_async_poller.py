# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import logging
from collections.abc import Awaitable
from typing import Callable, Any, Tuple, Generic, TypeVar, Generator

from ..exceptions import AzureError
from ._poller import NoPolling as _NoPolling


PollingReturnType_co = TypeVar("PollingReturnType_co", covariant=True)

_LOGGER = logging.getLogger(__name__)


class AsyncPollingMethod(Generic[PollingReturnType_co]):
    """ABC class for polling method."""

    def initialize(self, client: Any, initial_response: Any, deserialization_callback: Any) -> None:
        raise NotImplementedError("This method needs to be implemented")

    async def run(self) -> None:
        raise NotImplementedError("This method needs to be implemented")

    def status(self) -> str:
        raise NotImplementedError("This method needs to be implemented")

    def finished(self) -> bool:
        raise NotImplementedError("This method needs to be implemented")

    def resource(self) -> PollingReturnType_co:
        raise NotImplementedError("This method needs to be implemented")

    def get_continuation_token(self) -> str:
        raise TypeError("Polling method '{}' doesn't support get_continuation_token".format(self.__class__.__name__))

    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs) -> Tuple[Any, Any, Callable]:
        raise TypeError("Polling method '{}' doesn't support from_continuation_token".format(cls.__name__))


class AsyncNoPolling(_NoPolling):
    """An empty async poller that returns the deserialized initial response."""

    async def run(self):  # pylint:disable=invalid-overridden-method
        """Empty run, no polling.
        Just override initial run to add "async"
        """


async def async_poller(client, initial_response, deserialization_callback, polling_method):
    """Async Poller for long running operations.

    .. deprecated:: 1.5.0
       Use :class:`AsyncLROPoller` instead.

    :param client: A pipeline service client.
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.PipelineResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.PollingMethod
    """
    poller = AsyncLROPoller(client, initial_response, deserialization_callback, polling_method)
    return await poller


class AsyncLROPoller(Generic[PollingReturnType_co], Awaitable):
    """Async poller for long running operations.

    :param client: A pipeline service client
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.PipelineResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.AsyncPollingMethod
    """

    def __init__(
        self,
        client: Any,
        initial_response: Any,
        deserialization_callback: Callable,
        polling_method: AsyncPollingMethod[PollingReturnType_co],
    ):
        self._polling_method = polling_method
        self._done = False

        # This implicit test avoids bringing in an explicit dependency on Model directly
        try:
            deserialization_callback = deserialization_callback.deserialize  # type: ignore
        except AttributeError:
            pass

        self._polling_method.initialize(client, initial_response, deserialization_callback)

    def polling_method(self) -> AsyncPollingMethod[PollingReturnType_co]:
        """Return the polling method associated to this poller."""
        return self._polling_method

    def continuation_token(self) -> str:
        """Return a continuation token that allows to restart the poller later.

        :returns: An opaque continuation token
        :rtype: str
        """
        return self._polling_method.get_continuation_token()

    @classmethod
    def from_continuation_token(
        cls, polling_method: AsyncPollingMethod[PollingReturnType_co], continuation_token: str, **kwargs
    ) -> "AsyncLROPoller[PollingReturnType_co]":
        (
            client,
            initial_response,
            deserialization_callback,
        ) = polling_method.from_continuation_token(continuation_token, **kwargs)
        return cls(client, initial_response, deserialization_callback, polling_method)

    def status(self) -> str:
        """Returns the current status string.

        :returns: The current status string
        :rtype: str
        """
        return self._polling_method.status()

    async def result(self) -> PollingReturnType_co:
        """Return the result of the long running operation.

        :returns: The deserialized resource of the long running operation, if one is available.
        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
        await self.wait()
        return self._polling_method.resource()

    def __await__(self) -> Generator[Any, None, PollingReturnType_co]:
        return self.result().__await__()

    async def wait(self) -> None:
        """Wait on the long running operation.

        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
        try:
            await self._polling_method.run()
        except AzureError as error:
            if not error.continuation_token:
                try:
                    error.continuation_token = self.continuation_token()
                except Exception as err:  # pylint: disable=broad-except
                    _LOGGER.warning("Unable to retrieve continuation token: %s", err)
                    error.continuation_token = None
            raise
        self._done = True

    def done(self) -> bool:
        """Check status of the long running operation.

        :returns: 'True' if the process has completed, else 'False'.
        :rtype: bool
        """
        return self._done
