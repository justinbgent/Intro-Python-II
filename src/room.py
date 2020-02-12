# Implement a class to hold room information. This should have name and
# description attributes.
import room

class Room:
    n_to = 0
    e_to = 0
    s_to = 0
    w_to = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def canPlayerMoveThere(self, direction):
        if direction == "n":
            if(self.n_to == 0):
                print("ERROR: Can't move that direction here.")
                return False
            else:
                return True
        if direction == "e":
            if(self.e_to == 0):
                print("ERROR: Can't move that direction here.")
                return False
            else:
                return True
        if direction == "s":
            if(self.s_to == 0):
                print("ERROR: Can't move that direction here.")
                return False
            else:
                return True
        if direction == "w":
            if(self.w_to == 0):
                print("ERROR: Can't move that direction here.")
                return False
            else:
                return True
    
    def __str__(self):
        return (self.description + "\nLocation: \"" + self.name + "\"")

    def __repr__(self):
        return ("\nEntered " + self.name + ". " + self.description)