# from cc import turtle, gps
from computercraft.subapis import turtle, gps
from typing import Union

class GPSError(Exception):
    def __init__(self, message="Could not triangulate location!"):
        super().__init__(self.message)

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



def move(direction: str = "forward", distance: int = 1, turn: Union[str, None] = None, *args: tuple) -> None:
    
    directionDict: dict
    directionDict = {
        "up": turtle.up,
        "down": turtle.down,
        "forward": turtle.forward
    }

    if (distance < 1):
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

    for i in range(abs(distance)):
        for function in args:
            function()
        directionDict[direction.lower()]()

def getDirection() -> str:
    previousCoords: Union[tuple, None]
    previousCoords = gps.locate()
    #tuples => (x, y, z)

    if (previousCoords):
        if turtle.detect():
            turtle.dig()
        move()
        newCoords: Union[tuple, None]
        newCoords = gps.locate()
        if (newCoords):
            if (newCoords[0] > previousCoords[0]):
                return '+x'
            elif (newCoods[0] < previousCoords[0]):
                return '-x'
            if (newCoords[2] > previousCoords[2]):
                return '+z'
            elif (newCoods[2] < previousCoords[2]):
                return '-z'
        else:
            raise GPSError
    else:
        raise GPSError

def goTo(x: int, y: int, z: int) -> None:
    
    coords: Union[tuple, None]
    coords = gps.locate()
    if (coords):
       pass
    else:
        raise GPSError

