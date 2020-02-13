from room import Room

# Declare all the rooms

from item import Item
outsideItems, foyerItems, overlookItems, narrowItems = list(), list(), list(), list()
outsideItems.append(Item("Key", "This key looks old. Maybe it unlocks something."))
foyerItems.append(Item("Nothing", "This room looks empty. May as well move on."))
overlookItems.append(Item("Ladder", "You might be able to climb down somewhere with this."))
narrowItems.append(Item("Dust", "This seems useless."))

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons.", outsideItems),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", foyerItems),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlookItems),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrowItems),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", list()),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
from player import Player
player = Player("You", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
play = True
justOnce = True

def getInput():
    action = input("What would you like to do? Action: ")
    print("\n")
    if action == "q":
        global play 
        global justOnce
        play = False
    elif action == "n":
        if player.currentRoom.canPlayerMoveThere("n") == True:
            player.currentRoom = player.currentRoom.n_to
    elif action == "e":
        if player.currentRoom.canPlayerMoveThere("e") == True:
            player.currentRoom = player.currentRoom.e_to
    elif action == "s":
        if player.currentRoom.canPlayerMoveThere("s") == True:
            player.currentRoom = player.currentRoom.s_to
    elif action == "w":
        if player.currentRoom.canPlayerMoveThere("w") == True:
            player.currentRoom = player.currentRoom.w_to
    elif action == "i" or action == "inventory":
        print("Inventory: ")
        for item in player.inventory: print(" -" + item.name)
    elif action == "c":
        justOnce = True
    elif action.__contains__("drop"):
        player.dropItem(action[5:])
    elif action.__contains__("take"):
        player.takeItem(action[5:])
    elif action.__contains__("get"):
        player.takeItem(action[4:])
    else:
        print(f"\n'{action}' is not valid input")
        getInput()

while play:
    if justOnce:
        justOnce = False
        print("Use 'take' 'get' or 'drop' followed by 'itemName' to use player inventory\n" +
        "'n' 'e' 's' or 'w' to go north, east, south, or west.\n" +
        "'q' to quit 'c' to show controls again")
    print("\n" + player.currentRoom.__str__())
    if len(player.currentRoom.items) != 0:
        print("This room has: ")
        for item in player.currentRoom.items: print(" -" + item.name)
    getInput()
    