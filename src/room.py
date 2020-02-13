# Implement a class to hold room information. This should have name and
# description attributes.
import room

class Room:
    n_to = 0
    e_to = 0
    s_to = 0
    w_to = 0

    from item import Item
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def moveReport(self, travelAttempt, stringToCheckAgainst, valueCheck):
        if travelAttempt == stringToCheckAgainst:
            if(valueCheck == 0):
                print("\nERROR: Can't move that direction here.")
                return False
            else:
                return True
        

    def canPlayerMoveThere(self, direction):
        return (self.moveReport(direction, "n", self.n_to) or 
        self.moveReport(direction, "e", self.e_to) or
        self.moveReport(direction, "s", self.s_to) or
        self.moveReport(direction, "w", self.w_to))
    
    def __str__(self):
        return (self.description + "\nLocation: \"" + self.name + "\"")

    def __repr__(self):
        return ("\nEntered " + self.name + ". " + self.description)