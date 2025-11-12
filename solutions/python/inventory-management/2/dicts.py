"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory_dict = {}
    return update_dict(inventory_dict, items)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    return update_dict(inventory, items)

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        item_from_inventory = inventory.get(item, "DNE")
        if item_from_inventory != "DNE" and item_from_inventory > 0:
            inventory[item] -= 1
    
    return inventory
    


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item, "DNE") != "DNE":
        inventory.pop(item)

    return inventory
        


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []
    for item in inventory:
        if inventory.get(item, 0) > 0:
            inventory_list.append((item, inventory[item]))
    return inventory_list

def update_dict(dictionary, items):
    for item in items:
        if dictionary.get(item, "DNE") == "DNE":
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary
