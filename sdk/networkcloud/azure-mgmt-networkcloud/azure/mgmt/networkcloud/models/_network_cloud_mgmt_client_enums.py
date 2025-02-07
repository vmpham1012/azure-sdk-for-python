# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class BareMetalMachineCordonStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The cordon status of the bare metal machine."""

    CORDONED = "Cordoned"
    UNCORDONED = "Uncordoned"


class BareMetalMachineDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the bare metal machine."""

    PREPARING = "Preparing"
    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"


class BareMetalMachineEvacuate(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether to evacuate the node workload when the bare metal machine is cordoned."""

    TRUE = "True"
    FALSE = "False"


class BareMetalMachineHardwareValidationCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The category of hardware validation to perform."""

    BASIC_VALIDATION = "BasicValidation"


class BareMetalMachineHardwareValidationResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The outcome of the hardware validation."""

    PASS = "Pass"
    FAIL = "Fail"
    PASS_ENUM = "Pass"


class BareMetalMachineKeySetDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the key set."""

    ALL_ACTIVE = "AllActive"
    SOME_INVALID = "SomeInvalid"
    ALL_INVALID = "AllInvalid"
    VALIDATING = "Validating"


class BareMetalMachineKeySetPrivilegeLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The access level allowed for the users in this key set."""

    STANDARD = "Standard"
    SUPERUSER = "Superuser"


class BareMetalMachineKeySetProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the bare metal machine key set."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    PROVISIONING = "Provisioning"


class BareMetalMachineKeySetUserSetupStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the user is currently deployed for access."""

    ACTIVE = "Active"
    INVALID = "Invalid"


class BareMetalMachinePowerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The power state derived from the baseboard management controller."""

    ON = "On"
    OFF = "Off"


class BareMetalMachineProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the bare metal machine."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class BareMetalMachineReadyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the bare metal machine is ready to receive workloads."""

    TRUE = "True"
    FALSE = "False"


class BareMetalMachineSkipShutdown(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether to skip the graceful OS shutdown and power off the bare metal machine
    immediately.
    """

    TRUE = "True"
    FALSE = "False"


class BmcKeySetDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the key set."""

    ALL_ACTIVE = "AllActive"
    SOME_INVALID = "SomeInvalid"
    ALL_INVALID = "AllInvalid"
    VALIDATING = "Validating"


class BmcKeySetPrivilegeLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The access level allowed for the users in this key set."""

    READ_ONLY = "ReadOnly"
    ADMINISTRATOR = "Administrator"


class BmcKeySetProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the baseboard management controller key set."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    PROVISIONING = "Provisioning"


class BootstrapProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of bootstrap protocol used."""

    PXE = "PXE"


class CloudServicesNetworkDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the cloud services network."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class CloudServicesNetworkEnableDefaultEgressEndpoints(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the platform default endpoints are allowed for the egress traffic."""

    TRUE = "True"
    FALSE = "False"


class CloudServicesNetworkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the cloud services network."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class ClusterConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The latest heartbeat status between the cluster manager and the cluster."""

    CONNECTED = "Connected"
    TIMEOUT = "Timeout"
    UNDEFINED = "Undefined"


class ClusterDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current detailed status of the cluster."""

    PENDING_DEPLOYMENT = "PendingDeployment"
    DEPLOYING = "Deploying"
    RUNNING = "Running"
    UPDATING = "Updating"
    DEGRADED = "Degraded"
    DELETING = "Deleting"
    DISCONNECTED = "Disconnected"
    FAILED = "Failed"


class ClusterManagerConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The latest connectivity status between cluster manager and the cluster."""

    CONNECTED = "Connected"
    UNREACHABLE = "Unreachable"


class ClusterManagerDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The detailed status that provides additional information about the cluster manager."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"
    PROVISIONING_FAILED = "ProvisioningFailed"
    UPDATING = "Updating"
    UPDATE_FAILED = "UpdateFailed"


class ClusterManagerProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the cluster manager."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"
    UPDATING = "Updating"


class ClusterMetricsConfigurationDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the metrics configuration."""

    PROCESSING = "Processing"
    APPLIED = "Applied"
    ERROR = "Error"


class ClusterMetricsConfigurationProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the metrics configuration."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    PROVISIONING = "Provisioning"


class ClusterProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the cluster."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    VALIDATING = "Validating"
    UPDATING = "Updating"


class ClusterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of rack configuration for the cluster."""

    SINGLE_RACK = "SingleRack"
    MULTI_RACK = "MultiRack"


class ConsoleDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the console."""

    READY = "Ready"
    ERROR = "Error"


class ConsoleEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The credentials used to login to the image repository that has access to the specified image."""

    TRUE = "True"
    FALSE = "False"


class ConsoleProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the virtual machine console."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class ControlImpact(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the control plane will be impacted during the upgrade."""

    TRUE = "True"
    FALSE = "False"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DefaultCniNetworkDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the default CNI network."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class DefaultCniNetworkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the default CNI network."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class DefaultGateway(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether this is the default gateway.
    Only one of the attached networks (including the CloudServicesNetwork attachment) for a single
    machine may be specified as True.
    """

    TRUE = "True"
    FALSE = "False"


class DeviceConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The connection type of the device."""

    PCI = "PCI"


class DiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The disk type of rack SKU resource."""

    HDD = "HDD"
    SSD = "SSD"


class HybridAksClusterDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of this Hybrid AKS cluster."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class HybridAksClusterMachinePowerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The power state (On | Off) of the node."""

    ON = "On"
    OFF = "Off"


class HybridAksClusterProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the Hybrid AKS cluster resource."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class HybridAksIpamEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether or not to disable IPAM allocation on the network attachment definition
    injected into the Hybrid AKS Cluster.
    """

    TRUE = "True"
    FALSE = "False"


class HybridAksPluginType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network plugin type for Hybrid AKS."""

    DPDK = "DPDK"
    SRIOV = "SRIOV"
    OS_DEVICE = "OSDevice"


class IpAllocationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the IP address allocation."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUAL_STACK = "DualStack"


class L2NetworkDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the L2 network."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class L2NetworkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the L2 network."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class L3NetworkDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the L3 network."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class L3NetworkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the L3 network."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class MachineSkuDiskConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The connection type of the rack SKU resource."""

    PCIE = "PCIE"
    SATA = "SATA"
    RAID = "RAID"
    SAS = "SAS"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class OsDiskCreateOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The strategy for creating the OS disk."""

    EPHEMERAL = "Ephemeral"


class OsDiskDeleteOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The strategy for deleting the OS disk."""

    DELETE = "Delete"


class RackDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the rack."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class RackProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the rack resource."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class RackSkuProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the rack SKU resource."""

    SUCCEEDED = "Succeeded"


class RackSkuType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the rack."""

    AGGREGATOR = "Aggregator"
    COMPUTE = "Compute"
    SINGLE = "Single"


class RemoteVendorManagementFeature(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the storage appliance supports remote vendor management."""

    SUPPORTED = "Supported"
    UNSUPPORTED = "Unsupported"


class RemoteVendorManagementStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the remote vendor management feature is enabled or disabled, or
    unsupported if it is an unsupported feature.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    UNSUPPORTED = "Unsupported"


class SkipShutdown(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether to skip the graceful OS shutdown and power off the virtual machine
    immediately.
    """

    TRUE = "True"
    FALSE = "False"


class StorageApplianceDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The detailed status of the storage appliance."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class StorageApplianceHardwareValidationCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The category of hardware validation to perform."""

    BASIC_VALIDATION = "BasicValidation"


class StorageApplianceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the storage appliance."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class TrunkedNetworkDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the trunked network."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class TrunkedNetworkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the trunked network."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class ValidationThresholdGrouping(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Selection of how the type evaluation is applied to the cluster calculation."""

    PER_CLUSTER = "PerCluster"
    PER_RACK = "PerRack"


class ValidationThresholdType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Selection of how the threshold should be evaluated."""

    COUNT_SUCCESS = "CountSuccess"
    PERCENT_SUCCESS = "PercentSuccess"


class VirtualMachineBootMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Selects the boot method for the virtual machine."""

    UEFI = "UEFI"
    BIOS = "BIOS"


class VirtualMachineDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the virtual machine."""

    ERROR = "Error"
    AVAILABLE = "Available"
    PROVISIONING = "Provisioning"


class VirtualMachineDeviceModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the device model to use."""

    T1 = "T1"
    T2 = "T2"


class VirtualMachineIPAllocationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IP allocation mechanism for the virtual machine.
    Dynamic and Static are only valid for l3Network which may also specify Disabled.
    Otherwise, Disabled is the only permitted value.
    """

    DYNAMIC = "Dynamic"
    STATIC = "Static"
    DISABLED = "Disabled"


class VirtualMachineIsolateEmulatorThread(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Field Deprecated, the value will be ignored if provided. The indicator of whether one of the
    specified CPU cores is isolated to run the emulator thread for this virtual machine.
    """

    TRUE = "True"
    FALSE = "False"


class VirtualMachinePlacementHintPodAffinityScope(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scope for the virtual machine affinity or anti-affinity placement hint. It should always be
    "Machine" in the case of node affinity.
    """

    RACK = "Rack"
    MACHINE = "Machine"


class VirtualMachinePlacementHintType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The specification of whether this hint supports affinity or anti-affinity with the referenced
    resources.
    """

    AFFINITY = "Affinity"
    ANTI_AFFINITY = "AntiAffinity"


class VirtualMachinePowerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The power state of the virtual machine."""

    ON = "On"
    OFF = "Off"


class VirtualMachineProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the virtual machine."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class VirtualMachineSchedulingExecution(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the hint is a hard or soft requirement during scheduling."""

    HARD = "Hard"
    SOFT = "Soft"


class VirtualMachineVirtioInterfaceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Field Deprecated, use virtualizationModel instead. The type of the virtio interface."""

    MODERN = "Modern"
    TRANSITIONAL = "Transitional"


class VolumeDetailedStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The more detailed status of the volume."""

    ERROR = "Error"
    ACTIVE = "Active"
    PROVISIONING = "Provisioning"


class VolumeProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the volume."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    ACCEPTED = "Accepted"


class WorkloadImpact(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The indicator of whether the workload will be impacted during the upgrade."""

    TRUE = "True"
    FALSE = "False"
