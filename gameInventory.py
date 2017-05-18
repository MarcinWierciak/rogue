from csv import reader
import csv


# Displays the inventory
def display_inventory(inventory):
    print("Inventory:")
    amount = 0
    for key,value in inventory.items():
        amount += int(value)
        print(value, key)
    print("Total number of items:",amount)
    return amount


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item == "❀":
            item += ' flower'
        if item == "🍶":
            item += ' bottle'
        if item == "💰":
            item += ' money'
        if item == "🌟":
            item += ' star'
        if item == "🔑":
            item = "🔑"
            print(item)
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory



def print_table(inventory, order = None):
    print("Inventory:")

    if order == 'count,desc':
        sorted_dict = sorted(inventory, key=inventory.get, reverse=True)
    elif order == 'count,asc':
        sorted_dict = sorted(inventory, key=inventory.get, reverse=False)
    elif order == None:
        sorted_dict = list(inventory.keys())

        for item in sorted_dict:
            lenght = len(max(inventory,key = len))
        print("{:>{lenght}}".format("count", lenght =lenght - 4), "{:>{lenght}}".format("item name", lenght=lenght + 4))
        print('-'*lenght*2 + '-')

        for item in sorted_dict:
            print("{:>{lenght}}".format(inventory[item], lenght = lenght - 4), "{:>{lenght}}".format(item,lenght = lenght + 4))

        amount = 0
        for key,value in inventory.items():
            amount += int(value)
        print("Total number of items:",amount)



# Imports new inventory items from a file
def import_inventory(inventory, filename='test_inventory.csv'):
    with open(filename) as csv_file:
        freader = reader(csv_file, delimiter=",")
        imported_data = []
        for row in freader:
            for item in row:
                imported_data.append(item)
        add_to_inventory(inventory, imported_data)
    return inventory


# Exports the inventory into a .csv file.
def export_inventory(inventory, filename="test_inventory_export.csv"):
    with open(filename, 'w', newline= '') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',')
        items = []
        for key,value in inventory.items():
            items += [key]*value
        writer.writerow(items)



    #display_inventory(inv)
    #inv = add_to_inventory(inv, dragon_loot)
    #display_inventory(inv)
    #print_table(inv,'count,desc')
    #inv = import_inventory(inv)
    #print_table(inv)
    #export_inventory(inv)

if __name__ == '__main__':
    main()
