# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['managednetwork mn'] = """
    type: group
    short-summary: managednetwork mn
"""

helps['managednetwork mn list'] = """
    type: command
"""
"    short-summary: The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the"
" current subscription in a paginated format."
"""
    examples:
      - name: Get Managed Network
        text: |-
               az managednetwork mn list --resource-group "myResourceGroup"
"""

helps['managednetwork mn show'] = """
    type: command
"""
"    short-summary: The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group "
"and Managed Network name"
"""
    examples:
      - name: Get Managed Network
        text: |-
               az managednetwork mn show --managed-network-name "myManagedNetwork" --resource-group
               "myResourceGroup"
"""

helps['managednetwork mn create'] = """
    type: command
"""
"    short-summary: The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource"
" group and Managed Network name"
"""
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork mn create --location "eastus" --properties "{\\"scope\\":{\\"managementGrou
               ps\\":[{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20000000-0001-0000-0000-0
               00000000000\\"},{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20000000-0002-00
               00-0000-000000000000\\"}],\\"subnets\\":[{\\"id\\":\\"/subscriptions/subscriptionC/resourceGroup
               s/myResourceGroup/providers/Microsoft.Network/virtualNetworks/VnetC/subnets/subnetA\\"},{\\"
               id\\":\\"/subscriptions/subscriptionC/resourceGroups/myResourceGroup/providers/Microsoft.Net
               work/virtualNetworks/VnetC/subnets/subnetB\\"}],\\"subscriptions\\":[{\\"id\\":\\"subscriptionA\\
               "},{\\"id\\":\\"subscriptionB\\"}],\\"virtualNetworks\\":[{\\"id\\":\\"/subscriptions/subscriptionC
               /resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/VnetA\\"},{\\"id
               \\":\\"/subscriptions/subscriptionC/resourceGroups/myResourceGroup/providers/Microsoft.Netwo
               rk/virtualNetworks/VnetB\\"}]}}" --managed-network-name "myManagedNetwork"
               --resource-group "myResourceGroup"
"""

helps['managednetwork mn update'] = """
    type: command
    short-summary: Updates the specified Managed Network resource tags.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork mn update --managed-network-name "myManagedNetwork" --resource-group
               "myResourceGroup"
"""

helps['managednetwork mn delete'] = """
    type: command
"""
"    short-summary: The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource"
" group and Managed Network name"
"""
    examples:
      - name: Delete Managed Network
        text: |-
               az managednetwork mn delete --managed-network-name "myManagedNetwork" --resource-group
               "myResourceGroup"
"""

helps['managednetwork scope-assignment'] = """
    type: group
    short-summary: managednetwork scope-assignment
"""

helps['managednetwork scope-assignment list'] = """
    type: command
    short-summary: Get the specified scope assignment.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork scope-assignment list --scope "subscriptions/subscriptionC"
"""

helps['managednetwork scope-assignment show'] = """
    type: command
    short-summary: Get the specified scope assignment.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork scope-assignment show --scope "subscriptions/subscriptionC"
               --scope-assignment-name "subscriptionCAssignment"
"""

helps['managednetwork scope-assignment create'] = """
    type: command
    short-summary: Creates a scope assignment.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork scope-assignment create --properties-assigned-managed-network "/subscrip
               tions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/mana
               gedNetworks/myManagedNetwork" --scope "subscriptions/subscriptionC"
               --scope-assignment-name "subscriptionCAssignment"
"""

helps['managednetwork scope-assignment update'] = """
    type: command
    short-summary: Creates a scope assignment.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork scope-assignment create --properties-assigned-managed-network "/subscrip
               tions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/mana
               gedNetworks/myManagedNetwork" --scope "subscriptions/subscriptionC"
               --scope-assignment-name "subscriptionCAssignment"
"""

helps['managednetwork scope-assignment delete'] = """
    type: command
    short-summary: Deletes a scope assignment.
    examples:
      - name: Create/Update Managed Network
        text: |-
               az managednetwork scope-assignment delete --scope "subscriptions/subscriptionC"
               --scope-assignment-name "subscriptionCAssignment"
"""

helps['managednetwork managed-network-group'] = """
    type: group
    short-summary: managednetwork managed-network-group
"""

helps['managednetwork managed-network-group list'] = """
    type: command
"""
"    short-summary: The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in "
"a specified Managed Networks in a paginated format."
"""
    examples:
      - name: Get Managed Network Group
        text: |-
               az managednetwork managed-network-group list --managed-network-name "myManagedNetwork"
               --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-group show'] = """
    type: command
"""
"    short-summary: The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group"
", Managed Network name, and group name"
"""
    examples:
      - name: Get Managed Network Group
        text: |-
               az managednetwork managed-network-group show --group-name "myManagedNetworkGroup1"
               --managed-network-name "myManagedNetwork" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-group create'] = """
    type: command
    short-summary: The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource
    examples:
      - name: Create/Update Managed Network Group
        text: |-
               az managednetwork managed-network-group create --properties-management-groups "[]"
               --properties-subnets id=/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.\\
               Network/virtualNetworks/VnetA/subnets/subnetA --properties-virtual-networks id=/subscripti\\
               onB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/VnetA
               --properties-virtual-networks id=/subscriptionB/resourceGroups/myResourceGroup/providers/M\\
               icrosoft.Network/virtualNetworks/VnetB --group-name "myManagedNetworkGroup1"
               --managed-network-name "myManagedNetwork" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-group update'] = """
    type: command
    short-summary: The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource
    examples:
      - name: Create/Update Managed Network Group
        text: |-
               az managednetwork managed-network-group create --properties-management-groups "[]"
               --properties-subnets id=/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.\\
               Network/virtualNetworks/VnetA/subnets/subnetA --properties-virtual-networks id=/subscripti\\
               onB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/VnetA
               --properties-virtual-networks id=/subscriptionB/resourceGroups/myResourceGroup/providers/M\\
               icrosoft.Network/virtualNetworks/VnetB --group-name "myManagedNetworkGroup1"
               --managed-network-name "myManagedNetwork" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-group delete'] = """
    type: command
"""
"    short-summary: The Delete ManagedNetworkGroups operation deletes a Managed Network Group specified by the resource"
" group, Managed Network name, and group name"
"""
    examples:
      - name: Delete Managed Network Group
        text: |-
               az managednetwork managed-network-group delete --group-name "myManagedNetworkGroup1"
               --managed-network-name "myManagedNetwork" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-peering-policy'] = """
    type: group
    short-summary: managednetwork managed-network-peering-policy
"""

helps['managednetwork managed-network-peering-policy list'] = """
    type: command
"""
"    short-summary: The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Polici"
"es in a specified Managed Network, in a paginated format."
"""
    examples:
      - name: Get Managed Network Group
        text: |-
               az managednetwork managed-network-peering-policy list --managed-network-name
               "myManagedNetwork" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-peering-policy show'] = """
    type: command
"""
"    short-summary: The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, spe"
"cified by the  resource group, Managed Network name, and peering policy name"
"""
    examples:
      - name: Get Managed Network Peering Policy
        text: |-
               az managednetwork managed-network-peering-policy show --managed-network-name
               "myManagedNetwork" --policy-name "myHubAndSpoke" --resource-group "myResourceGroup"
"""

helps['managednetwork managed-network-peering-policy create'] = """
    type: command
"""
"    short-summary: The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Polic"
"y"
"""
    examples:
      - name: Create/Update Managed Network Peering Policy
        text: |-
               az managednetwork managed-network-peering-policy create --managed-network-name
               "myManagedNetwork" --policy-name "myHubAndSpoke" --properties "{\\"type\\":\\"HubAndSpokeTopo
               logy\\",\\"hub\\":{\\"id\\":\\"/subscriptions/subscriptionB/resourceGroups/myResourceGroup/provi
               ders/Microsoft.Network/virtualNetworks/myHubVnet\\"},\\"spokes\\":[{\\"id\\":\\"/subscriptions/s
               ubscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/managedNetw
               orks/myManagedNetwork/managedNetworkGroups/myManagedNetworkGroup1\\"}]}" --resource-group
               "myResourceGroup"
"""

helps['managednetwork managed-network-peering-policy update'] = """
    type: command
"""
"    short-summary: The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Polic"
"y"
"""
    examples:
      - name: Create/Update Managed Network Peering Policy
        text: |-
               az managednetwork managed-network-peering-policy create --managed-network-name
               "myManagedNetwork" --policy-name "myHubAndSpoke" --properties "{\\"type\\":\\"HubAndSpokeTopo
               logy\\",\\"hub\\":{\\"id\\":\\"/subscriptions/subscriptionB/resourceGroups/myResourceGroup/provi
               ders/Microsoft.Network/virtualNetworks/myHubVnet\\"},\\"spokes\\":[{\\"id\\":\\"/subscriptions/s
               ubscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/managedNetw
               orks/myManagedNetwork/managedNetworkGroups/myManagedNetworkGroup1\\"}]}" --resource-group
               "myResourceGroup"
"""

helps['managednetwork managed-network-peering-policy delete'] = """
    type: command
"""
"    short-summary: The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specif"
"ied by the  resource group, Managed Network name, and peering policy name"
"""
    examples:
      - name: Get Managed Network Peering Policy
        text: |-
               az managednetwork managed-network-peering-policy delete --managed-network-name
               "myManagedNetwork" --policy-name "myHubAndSpoke" --resource-group "myResourceGroup"
"""
