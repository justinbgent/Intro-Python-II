from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

def getInput():
    continueGame = input("What would you like to do? ('n' 'e' 's' or 'w' to go north, east, south, or west. 'q' to quit)\n:")
    if continueGame == "q":
        global play 
        play = False
    elif continueGame == "n":
        if player.currentRoom.canPlayerMoveThere("n") == True:
            player.currentRoom = player.currentRoom.n_to
    elif continueGame == "e":
        if player.currentRoom.canPlayerMoveThere("e") == True:
            player.currentRoom = player.currentRoom.e_to
    elif continueGame == "s":
        if player.currentRoom.canPlayerMoveThere("s") == True:
            player.currentRoom = player.currentRoom.s_to
    elif continueGame == "w":
        if player.currentRoom.canPlayerMoveThere("w") == True:
            player.currentRoom = player.currentRoom.w_to
    else:
        print(f"\n'{continueGame}' is not valid input")
        getInput()

while play:
    print("\n" + player.currentRoom.__str__())
    getInput()
    