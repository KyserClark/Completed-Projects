# Inventories
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff_2 = {'gold coin': 42, 'rope': 1}

# Loot of defeated foes
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
troll_loot = ['gold coin', 'spike bat', 'shield', 'troll horn', 'troll horn',
              'arrow']


def display_inventory(inventory):
    """ Print out inventory in formatted way. """
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(f'\t{v} {k}')
        item_total += int(v)

    print("\nTotal number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    """ Take defeated foe's loot and add it to inventory. """
    for item in added_items:
        inventory.setdefault(item, 0)
        new_item_value = inventory[item] + 1
        inventory[item] = new_item_value


add_to_inventory(stuff, troll_loot)

display_inventory(stuff)
