from computercraft.subapis import import_file, gps, turtle, peripheral
# from cc import import_file, gps, turtle
from typing import Union
GPS = import_file('/utils/GPS.py')

class Turtle():

    """
    A class used to represent a Turtle, preserving the state throughout its journey.

    ...

    Attributes
    ----------
    name : str
        the name of the animal
    position : dict[str, int]
        the x, y and z of the turtle on the minecraft world
    direction : GPS.Direction
        the direction of the turtle

    Methods
    -------
    forward()
        Move the turtle forward one block.
    back()
        Move the turtle backwards one block.
    up()                  
        Move the turtle up one block.
    down()                
        Move the turtle down one block.
    turnLeft()       	    
        Rotate the turtle 90 degress to the left.
    turnRight()           
        Rotate the turtle 90 degress to the right.
    dig([side])	        
        Attempt to break the block in front of the turtle.
    digUp([side])	        
        Attempt to break the block above the turtle.
    digDown([side])	    
        Attempt to break the block below the turtle.
    place([text])	        
        Place a block or item into the world in front of the turtle.
    placeUp([text])	    
        Place a block or item into the world above the turtle.
    placeDown([text])	    
        Place a block or item into the world below the turtle.
    drop([count])	        
        Drop the currently selected stack into the inventory in front of the turtle, or as an item into the world if there is no inventory.
    dropUp([count])	    
        Drop the currently selected stack into the inventory above the turtle, or as an item into the world if there is no inventory.
    dropDown([count])	    
        Drop the currently selected stack into the inventory in front of the turtle, or as an item into the world if there is no inventory.
    select(slot)	        
        Change the currently selected slot.
    getItemCount([slot])	
        Get the number of items in the given slot.
    getItemSpace([slot])	
        Get the remaining number of items which may be stored in this stack.
    detect()	            
        Check if there is a solid block in front of the turtle.
    detectUp()	        
        Check if there is a solid block above the turtle.
    detectDown()	        
        Check if there is a solid block below the turtle.
    compare()	            
        Check if the block in front of the turtle is equal to the item in the currently selected slot.
    compareUp()	        
        Check if the block above the turtle is equal to the item in the currently selected slot.
    compareDown()	        
        Check if the block below the turtle is equal to the item in the currently selected slot.
    attack([side])	    
        Attack the entity in front of the turtle.
    attackUp([side])	    
        Attack the entity above the turtle.
    attackDown([side])	
        Attack the entity below the turtle.
    suck([count])	        
        Suck an item from the inventory in front of the turtle, or from an item floating in the world.
    suckUp([count])	    
        Suck an item from the inventory above the turtle, or from an item floating in the world.
    suckDown([count])	    
        Suck an item from the inventory below the turtle, or from an item floating in the world.
    getFuelLevel()	    
        Get the maximum amount of fuel this turtle currently holds.
    refuel([count])	    
        Refuel this turtle.
    compareTo(slot)	    
        Compare the item in the currently selected slot to the item in another slot.
    transferTo(slot [, count])	
        Move an item from the selected slot to another one.
    getSelectedSlot()	    
        Get the currently selected slot.
    getFuelLimit()	    
        Get the maximum amount of fuel this turtle can hold.
    equipLeft()	        
        Equip (or unequip) an item on the left side of this turtle.
    equipRight()	        
        Equip (or unequip) an item on the right side of this turtle.
    inspect()	            
        Get information about the block in front of the turtle.
    inspectUp()	        
        Get information about the block above the turtle.
    inspectDown()     	
        Get information about the block below the turtle.
    getItemDetail([slot [, detailed]])	
        Get detailed information about the items in the given slot.
    craft([limit=64])	    
        Craft a recipe based on the turtle's inventory.

    """

    name: str
    position: dict[str, int]
    direction: GPS.Direction

    def __init__(self) -> None:
        _pos = gps.locate()
        if (_pos):
            self.position = {"x": int(_pos[0]), "y": int(_pos[1]), "z": int(_pos[2])}
        else:
            raise GPS.GPSError('Could not get location of turtle on initialization.\nDid you install a wireless modem?')
        
        self.direction = self.getDirection()

    def move(self, direction: str = "forward", distance: int = 1, turn: Union[str, None] = None, *args: tuple) -> None:
    
        directionDict: dict
        directionDict = {
            "up": self.up,
            "down": self.down,
            "forward": self.forward,
            "back": self.down()
        }

        if (int(distance) < 0):
            raise ValueError('Distance can\'t be negative.')

        if (direction not in directionDict):
            raise ValueError('Invalid direction, you may only use "up", "down" or "forward".')

        if turn:
            if turn.lower() == "left":
                turtle.turnLeft()
            elif turn.lower() == "right":
                turtle.turnRight()
            else:
                raise ValueError('Invalid turn argument, turn must be "left" or "right".')

        for i in range(abs(int(distance))):
            for function in args:
                function()
            directionDict[direction.lower()]()

    def getDirection(self) -> GPS.Direction:
        previousCoords: Union[tuple, None]
        previousCoords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))
        #tuples => (x, y, z)

        if (previousCoords):
            if self.detect():
                self.dig()
            self.move()
            newCoords: Union[tuple, None]
            newCoords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))
            
            self.back()

            if (newCoords):
                if (newCoords[0] > previousCoords[0]):
                    return GPS.Direction('+x')
                elif (newCoords[0] < previousCoords[0]):
                    return GPS.Direction('-x')
                elif (newCoords[2] > previousCoords[2]):
                    return GPS.Direction('+z')
                elif (newCoords[2] < previousCoords[2]):
                    return GPS.Direction('-z')
                else:
                    raise GPS.GPSError('Something went wrong, the position of the turtle didn\'t change')
        else:
            raise GPS.GPSError('Could not get coords while trying to get directions.')

    def forward(self):
        if self.direction.sign() == '+':
            self.position[self.direction.axis()] += 1
        else:
            self.position[self.direction.axis()] -= 1

        return turtle.forward()
        

    def back(self):
        if self.direction.sign() == '+':
            self.position[self.direction.axis()] += 1
        else:
            self.position[self.direction.axis()] -= 1
        
        return turtle.back()

    def up(self):
        self.position["y"] += 1
        return turtle.up()

    def down(self):
        self.position["y"] -= 1
        return turtle.down()

    def turnLeft(self):
        self.direction = self.direction - 1
        turtle.turnLeft()

    def turnRight(self):
        self.direction = self.direction + 1
        turtle.turnRight()

    def dig(self ):
        return turtle.dig()

    def digUp(self ):
        return turtle.digUp()

    def digDown(self):
        return turtle.digDown()

    def place(self, text = None):
        return turtle.place(text)

    def placeUp(self, text):
        # TODO
        pass

    def placeDown(self, text):
        # TODO
        pass

    def drop(self, count):
        # TODO
        pass

    def dropUp(self, count):
        # TODO
        pass

    def dropDown(self, count):
        # TODO
        pass

    def select(self, slot):
        # TODO
        pass

    def getItemCount(self, slot):
        # TODO
        pass

    def getItemSpace(self, slot):
        # TODO
        pass

    def detect(self):
        # TODO
        pass

    def detectUp(self):
        # TODO
        pass

    def detectDown(self):
        # TODO
        pass

    def compare(self):
        # TODO
        pass

    def compareUp(self):
        # TODO
        pass

    def compareDown(self):
        # TODO
        pass

    def attack(self, side):
        # TODO
        pass

    def attackUp(self, side):
        # TODO
        pass

    def attackDown(self, side):
        # TODO
        pass

    def suck(self, count):
        # TODO
        pass

    def suckUp(self, count):
        # TODO
        pass

    def suckDown(self, count):
        # TODO
        pass

    def getFuelLevel(self):
        # TODO
        pass

    def refuel(self, count):
        # TODO
        pass

    def compareTo(self, slot):
        # TODO
        pass

    def transferTo(self, slot, count):
        # TODO
        pass

    def getSelectedSlot(self):
        # TODO
        pass

    def getFuelLimit(self):
        # TODO
        pass

    def equipLeft(self):
        # TODO
        pass

    def equipRight(self):
        # TODO
        pass

    def inspect(self):
        # TODO
        pass

    def inspectUp(self):
        # TODO
        pass

    def inspectDown(self):
        # TODO
        pass

    def getItemDetail(self, slot, detailed):
        # TODO
        pass

    def craft(self, limit=64):
        # TODO
        pass