stuff = {'rope':1,'torch':6,'gold':4910,'dagger':1,'arrow':12}

def displayInventory(stuff):
    print('Inventory:')
    item_total = 0
    for k,v in stuff.items():
        print( str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in inventory.keys():
            inventory.setdefault(addedItems[i],1)
        else:
            for k,v in inventory.items():
                if k == addedItems[i]:
                    inventory[k] = inventory[k]+1
    return inventory      
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin',  'gold coin', 'gold coin', 'rope']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
