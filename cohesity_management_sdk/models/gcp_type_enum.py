# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class GcpTypeEnum(object):

    """Implementation of the 'GcpType' enum.

    Specifies the entity type such as 'kIAMUser' if the environment is kGCP.
    Specifies the type of a GCP source entity.
    'kIAMUser' indicates a unique user within a GCP account.
    'kProject' represents compute resources and storage.
    'kRegion' indicates a geographical region in the global infrastructure.
    'kAvailabilityZone' indicates an availability zone within a region.
    'kVirtualMachine' indicates a Virtual Machine running in GCP environment.
    'kVPC' indicates a virtual private cloud (VPC) network within GCP.
    'kSubnet' indicates a subnet inside the VPC.
    'kNetworkSecurityGroup' represents a network security group.
    'kInstanceType' represents various machine types.

    Attributes:
        KIAMUSER: TODO: type description here.
        KPROJECT: TODO: type description here.
        KREGION: TODO: type description here.
        KAVAILABILITYZONE: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KVPC: TODO: type description here.
        KSUBNET: TODO: type description here.
        KNETWORKSECURITYGROUP: TODO: type description here.
        KINSTANCETYPE: TODO: type description here.

    """

    KIAMUSER = 'kIAMUser'

    KPROJECT = 'kProject'

    KREGION = 'kRegion'

    KAVAILABILITYZONE = 'kAvailabilityZone'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KVPC = 'kVPC'

    KSUBNET = 'kSubnet'

    KNETWORKSECURITYGROUP = 'kNetworkSecurityGroup'

    KINSTANCETYPE = 'kInstanceType'

