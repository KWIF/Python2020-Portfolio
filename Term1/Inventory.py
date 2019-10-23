#Hero's Inventory
import random

health = 100
attck = 2
deff = 0
mana = 50
inventory = ( )
if not inventory:
    print("You are Empty Handed.")

input("\nPress The Enter Key to Continue")

inventory_max = 10
inventory = ["Short Sword",
             "Dagger",
             "Holy Chestpiece",
             "Chain Leggings",
             "Knight's Shield",
             "Mana Potion",
             "Holy Water",
             "Healing Potion",
             "Double Crossed Black Boots",
             "Knight's Helmet"]

equipment = [ ]
if len (inventory) < inventory_max:
    x = inventory_max - len(inventory)
    print("You may have "+ str(x) +" more items")
else:
    print("You are out of Space!")

for item in inventory:
    if item == "Knight's Shield":
        equipment.append(item)
        inventory.remove(item)
        deff += 10
    if item == "Short Sword" :
        equipment.append(item)
        inventory.remove(item)
        attck += 5
    if item == "Holy Chestpiece":
        equipment.append(item)
        inventory.remove(item)
        deff += 20
    if item == "Healing Potion":
        health += 25
        inventory.remove(item)
    if item == "Mana Potion":
        mana += 25
        inventory.remove(item)

print("Health "+ str(health) +" Mana: " + str(mana) +
      " Attack: " + str(attck) +" Denfense: "+ str(deff))
inventory[-4] = "New Item"
print(inventory)
chestSize =random.randint(1,6)
chestItems=("gold" ,
       "Gems" ,
       "Gravity Gun",
       "HellHound Bait",
       "Moldy Bread",
       "Bird Spies",
       "3 Decks of Cards")

chest = [ ]
for item in chestItems:
    inventory.append(item)
print("You Found a Chest!!!    It Contains:")
print(chestItems)
if len (inventory) > inventory_max:
    print(inventory)
    x = len(inventory) - inventory_max
    print ("You need to drop "+ str(x) +" number of items")
    while x > 0:
        item = input("Pick a item to drop")
        inventory.remove(item)
        x -= 1
print("Item obtained")

inventory += chest
print("Your inventory is now:")
print(inventory)


if len (inventory) < inventory_max:
    x = inventory_max - len(inventory)
    print("You may have "+ str(x) +" more items")
else:
    print("You are out of Space!")
    print("Purchase new bag or throw out items")



print (item)
print(min("ZZx", "ZZy", "ZZa"))
