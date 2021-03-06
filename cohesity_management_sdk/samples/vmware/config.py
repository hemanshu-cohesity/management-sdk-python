#!/usr/bin/env python
# Copyright 2019 Cohesity Inc.
#
# Config file to get all the configurations to assist VMware related workflows.


from datetime import datetime

VM_CONFIG = {'prefix_name': 'vmware-vms',
             'memory': 1024,
             'num_vcpu': 1,
             'guest_id':'windows9Server64Guest',
             'version':'vmx-14',
             'nic_type': 'E1000',
             'net_name': 'VM Network',
             'data_store': 'cohesity_int_10456',
             'net_name': 'VM Network',
             'num_vms': 3,
             }

CLUSTER_USERNAME = 'cluster_admin'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
VCENTER_IP = 'vcenter_ip'
VCENTER_USERNAME = 'administrator'
VCENTER_PASSWORD = 'vcenter_password'
DEFAULT_PORT = 443

JOB = {'name':'vcenter-automation-backup',
       'policy_name': 'Bronze',
       'run_now': True
       }
RESTORE = {'name': 'Recover-VMs_{0}'.format(datetime.now().strftime(
                                                    "%Y_%B_%d_%H-%M%p")),
           'vm_list': [VM_CONFIG['prefix_name'] + '-' + str(num) for num in
               range(VM_CONFIG['num_vms'])],
           'vms_deleted': False}
