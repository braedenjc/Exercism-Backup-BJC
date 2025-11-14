"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        #check the value if it exists. if it doesn't, insert the key 'item' and give it value '0'
        current_cart[item] = current_cart.setdefault(item, 0) 
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return add_item({}, notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return sorted(cart.items())


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    #reminder: each item in the cart has a name key, and then the value [quantity, aisle, refrigeration]
    combined_dict = {} 

    #current plan: iterate over the combined_dict using keys, and then look up the list attached inside of aisle mapping.
    
    for key in cart.keys():
        #if the key doesn't exist, init with an empty list. Toss any returned value.
        combined_dict.setdefault(key, [])
        combined_dict[key].append(cart[key])
        combined_dict[key].extend(aisle_mapping[key])
        
    combined_dict = sorted(combined_dict.items(), reverse = True)
    return combined_dict


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key in fulfillment_cart.keys():
        #the first entry in the list attached to either dict key is the quantity.
        store_quantity = store_inventory[key][0]
        cart_quantity = fulfillment_cart[key][0] 
        store_quantity -= cart_quantity
        if store_quantity == 0:
            store_quantity = "Out of Stock"
        store_inventory[key][0] = store_quantity
    return store_inventory
