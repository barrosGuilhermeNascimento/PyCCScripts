# from cc import turtle, gps
from computercraft.subapis import turtle, gps
from typing import Union
import math

class GPSError(Exception):
    def __init__(self, message="Could not triangulate location!"):
        super().__init__(message)

class Direction():
    _internalDirection: str = ''
    __internalOrder = ['+z', '-x', '-z', '+x']

    def __init__(self, direction: str) -> None:
        if (direction not in ['+z', '-x', '-z', '+x']):
            raise ValueError(f'{direction} is not a valid Direction.')
        self._internalDirection = direction 
    
    def __add__(self, other) -> 'Direction':
        newOrder = self.__internalOrder[self.__internalOrder.index(self._internalDirection):] + self.__internalOrder[:self.__internalOrder.index(self._internalDirection)]
        return Direction(newOrder[other % len(self.__internalOrder)])

    def __sub__(self, other) -> 'Direction':
        newOrder = self.__internalOrder[self.__internalOrder.index(self._internalDirection):] + self.__internalOrder[:self.__internalOrder.index(self._internalDirection)]
        return Direction(newOrder[(other % len(self.__internalOrder)) - len(self.__internalOrder)])

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self._internalDirection == other._internalDirection
        return False

    def __str__(self) -> str:
        return self._internalDirection

    def __repr__(self) -> str:
        return str(self)

    def axis(self) -> str:
        return self._internalDirection[1]

    def sign(self) -> str:
        return self._internalDirection[0]


def digBlock(blockName: str) -> bool:

    levels: int
    levels = 0

    runned: bool
    runned = False

    information = turtle.inspect()

    if (information == None):
        return runned
    
    while True:
        if (information['name'] == blockName):
            runned = True
            turtle.digUp()
            turtle.up()
            levels = levels + 1
        elif (levels > 0):
            while (levels > 0):
                turtle.down()
                turtle.dig()
                levels = levels - 1
            
            levels = 0
        elif (levels == 0):
            return runned
        
        information = turtle.inspect()
       
def findItem(item: str) -> bool:
    for i in range(1, 17):
        itemDetail = turtle.getItemDetail(i)
        if (itemDetail != None):
            if (itemDetail['name'] == item):
                turtle.select(i)
                return True
    
    return False
        
def storeItems() -> None:

    onePack: bool
    onePack = False

    for i in range(1, 17):

        itemDetail: dict
        itemDetail = turtle.getItemDetail(i)

        if (itemDetail != None):
            if(itemDetail['name'] == "minecraft:oak_sapling"):
                if (onePack):
                    turtle.select(i)
                    turtle.drop()
                else:
                    onePack = True
                
            else:
                turtle.select(i)
                turtle.drop()
            
def findOcurrences(blockname: str) -> list:

    previousSelection: int
    previousSelection = turtle.getSelectedSlot()

    occurrences: list
    occurrences = []

    for i in range(1, 17):
        # turtle.select(i)
        if turtle.getItemDetail(i) != None:
            if turtle.getItemDetail(i)['name'] == blockname:
                occurrences.append(i)
        
    turtle.select(previousSelection)

    return occurrences


def findTotalCount(blockname: str) -> int:

    previousSelection: int
    previousSelection = turtle.getSelectedSlot()

    count: int
    count = 0

    for i in range(1, 17):
        # turtle.select(i)
        if turtle.getItemDetail(i) != None:
            if turtle.getItemDetail(i)['name'] == blockname:
                count = count + turtle.getItemDetail(i).count

    turtle.select(previousSelection)
    return count

def turn(direction: str, times: int = 1) -> None:
    directionDict = {
        "left": turtle.turnLeft,
        "right": turtle.turnRight,
    }

    if (direction not in directionDict):
        raise ValueError('Invalid direction, you may only use "left" or "right".')

    if (times < 0):
        raise ValueError('Times can\'t be negative.')

    for i in range(times):
        directionDict[direction]()

def move(direction: str = "forward", distance: int = 1, turn: Union[str, None] = None, *args: tuple) -> None:
    
    directionDict: dict
    directionDict = {
        "up": turtle.up,
        "down": turtle.down,
        "forward": turtle.forward
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

# Deprecated, instead call static method of the same name from Turtle class.
def getDirection() -> Direction:
    previousCoords: Union[tuple, None]
    previousCoords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))
    #tuples => (x, y, z)

    if (previousCoords):
        if turtle.detect():
            turtle.dig()
        move()
        newCoords: Union[tuple, None]
        newCoords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))
        
        turn('left', 2)
        move()
        turn('left', 2)

        if (newCoords):
            if (newCoords[0] > previousCoords[0]):
                return Direction('+x')
            elif (newCoords[0] < previousCoords[0]):
                return Direction('-x')
            elif (newCoords[2] > previousCoords[2]):
                return Direction('+z')
            elif (newCoords[2] < previousCoords[2]):
                return Direction('-z')
            else:
                raise GPSError('Something went wrong, the position of the turtle didn\'t change')
    else:
        raise GPSError

def faceDirection(currentDirection: Direction, direction: Direction) -> Direction:
    if (not isinstance(currentDirection, Direction) or not isinstance(direction, Direction)):
        raise ValueError('Invalid direction, you must pass a Direction class instance.')
    
    newDirection: Direction

    if (direction == currentDirection):
        return direction

    if (direction.axis() == currentDirection.axis()):
        for i in range(2):
            turtle.turnLeft()
    else:
        if ((currentDirection + 1) == direction):
            turtle.turnRight()
        else:
            turtle.turnLeft()

    return direction

def goTo(x: int, y: int, z: int, mode: str = "hard") -> None:
    if (mode.lower() not in ["hard", "soft"]):
        raise ValueError('This function only accepts \"hard\" or \"soft\" as its mode options.')

    facing: Direction
    facing = getDirection()

    coords: Union[tuple, None]
    coords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))

    for i in range(int(abs(y - coords[1]))):
        if (y - coords[1] > 0):
            if (mode == 'hard' and turtle.detectUp()):
                turtle.digUp()
            turtle.up()
        elif (y - coords[1] < 0):
            if (mode == 'hard' and turtle.detectDown()):
                turtle.digDown()
            turtle.down()

    while (x, y, z) != coords:
        if (coords and facing):
            if (x - coords[0] > 0):
                facing = faceDirection(facing, Direction('+x'))

            elif (x - coords[0] < 0):
                facing = faceDirection(facing, Direction('-x'))

            elif (z - coords[2] > 0):
                facing = faceDirection(facing, Direction('+z'))
            
            elif (z - coords[2] < 0):
                facing = faceDirection(facing, Direction('-z'))
                

            
            if (mode == 'hard' and turtle.detect()):
                turtle.dig()
            move()
            coords = (int(gps.locate()[0]), int(gps.locate()[1]), int(gps.locate()[2]))

    else:
        raise GPSError


    # to move in z AXIOS, need to look in x AXIOS    
    # if (facing x positive)
        # going to z negative
            #turnleft
        # going to z positive
            #turnright
    # if (facing x negative)
        # going to z negative
            #turnRight
        # going to z positive
            #turnLeft
            
    #if moving in x AXIOS
    # if (facing z positive)
        # goint to x negative
            # turnleft
    

