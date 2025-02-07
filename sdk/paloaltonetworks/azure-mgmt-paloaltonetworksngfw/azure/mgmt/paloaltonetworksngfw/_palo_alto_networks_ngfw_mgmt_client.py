# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import PaloAltoNetworksNgfwMgmtClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    CertificateObjectGlobalRulestackOperations,
    CertificateObjectLocalRulestackOperations,
    FirewallStatusOperations,
    FirewallsOperations,
    FqdnListGlobalRulestackOperations,
    FqdnListLocalRulestackOperations,
    GlobalRulestackOperations,
    LocalRulesOperations,
    LocalRulestacksOperations,
    Operations,
    PostRulesOperations,
    PreRulesOperations,
    PrefixListGlobalRulestackOperations,
    PrefixListLocalRulestackOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class PaloAltoNetworksNgfwMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """PaloAltoNetworksNgfwMgmtClient.

    :ivar global_rulestack: GlobalRulestackOperations operations
    :vartype global_rulestack: azure.mgmt.paloaltonetworksngfw.operations.GlobalRulestackOperations
    :ivar certificate_object_global_rulestack: CertificateObjectGlobalRulestackOperations
     operations
    :vartype certificate_object_global_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.CertificateObjectGlobalRulestackOperations
    :ivar fqdn_list_global_rulestack: FqdnListGlobalRulestackOperations operations
    :vartype fqdn_list_global_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.FqdnListGlobalRulestackOperations
    :ivar post_rules: PostRulesOperations operations
    :vartype post_rules: azure.mgmt.paloaltonetworksngfw.operations.PostRulesOperations
    :ivar prefix_list_global_rulestack: PrefixListGlobalRulestackOperations operations
    :vartype prefix_list_global_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.PrefixListGlobalRulestackOperations
    :ivar pre_rules: PreRulesOperations operations
    :vartype pre_rules: azure.mgmt.paloaltonetworksngfw.operations.PreRulesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.paloaltonetworksngfw.operations.Operations
    :ivar firewalls: FirewallsOperations operations
    :vartype firewalls: azure.mgmt.paloaltonetworksngfw.operations.FirewallsOperations
    :ivar local_rulestacks: LocalRulestacksOperations operations
    :vartype local_rulestacks: azure.mgmt.paloaltonetworksngfw.operations.LocalRulestacksOperations
    :ivar firewall_status: FirewallStatusOperations operations
    :vartype firewall_status: azure.mgmt.paloaltonetworksngfw.operations.FirewallStatusOperations
    :ivar certificate_object_local_rulestack: CertificateObjectLocalRulestackOperations operations
    :vartype certificate_object_local_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.CertificateObjectLocalRulestackOperations
    :ivar fqdn_list_local_rulestack: FqdnListLocalRulestackOperations operations
    :vartype fqdn_list_local_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.FqdnListLocalRulestackOperations
    :ivar local_rules: LocalRulesOperations operations
    :vartype local_rules: azure.mgmt.paloaltonetworksngfw.operations.LocalRulesOperations
    :ivar prefix_list_local_rulestack: PrefixListLocalRulestackOperations operations
    :vartype prefix_list_local_rulestack:
     azure.mgmt.paloaltonetworksngfw.operations.PrefixListLocalRulestackOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-08-29-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = PaloAltoNetworksNgfwMgmtClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.global_rulestack = GlobalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.certificate_object_global_rulestack = CertificateObjectGlobalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.fqdn_list_global_rulestack = FqdnListGlobalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.post_rules = PostRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.prefix_list_global_rulestack = PrefixListGlobalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.pre_rules = PreRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.firewalls = FirewallsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.local_rulestacks = LocalRulestacksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.firewall_status = FirewallStatusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificate_object_local_rulestack = CertificateObjectLocalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.fqdn_list_local_rulestack = FqdnListLocalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.local_rules = LocalRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.prefix_list_local_rulestack = PrefixListLocalRulestackOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "PaloAltoNetworksNgfwMgmtClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
