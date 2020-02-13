# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    inventory = list()

    from room import Room
    def __init__(self, name, currentRoom: Room):
        self.currentRoom = currentRoom

    from item import Item

    def takeItem(self, itemName):
        retrievedItem = False
        for item in self.currentRoom.items:
            if(item.name == itemName):
                retrievedItem = True
                self.inventory.append(item)
                self.currentRoom.items.remove(item)
                print(f"'{itemName}' added to your inventory.\n{item.description}")
                break
        if not retrievedItem:
            print(f"'{itemName}' is not in this room.")

    def dropItem(self, itemName):
        dropItem = False
        for item in self.inventory:
            if(item.name == itemName):
                dropItem = True
                self.inventory.remove(item)
                self.currentRoom.items.append(item)
                print(f"'{itemName}' dropped in room.")
                break
        if not dropItem:
            print(f"'{itemName}' is not in your inventory.")