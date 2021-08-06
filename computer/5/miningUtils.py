from typing import Union
# from computercraft.subapis import os, turtle
from cc import os, turtle

def refuelMiner() -> None:
    if (turtle.getFuelLevel() < 10):
        if (findItem("minecraft:coal")):
            turtle.refuel()

def findItem(item: str) -> bool:
    for i in range(1, 17):
        itemDetail = turtle.getItemDetail(i)
        if (itemDetail != None):
            if (itemDetail['name'] == item):
                turtle.select(i)
                return True
        else:
            return False
      
    return False


def digGravel() -> None:
    levels: int
    levels = 0

    information: Union[None, dict]
    information = turtle.inspect()
    print(information)

    if (information == None):
        return

    if (information['name'] == "minecraft:gravel"):
        turtle.digUp()
        turtle.up()
        levels += 1
    while levels >= 1:
        information = turtle.inspect()
        if (information == None):
            if(levels > 0):
                for i in range(levels):
                    turtle.dig()
                    turtle.down()
                levels = 0
        else:
            if (information['name'] == "minecraft:gravel"):
                turtle.digUp()
                turtle.up()
                levels += 1
            elif (levels > 0):
                for i in range(levels):
                    turtle.dig()
                    turtle.down()                    
                levels = 0
    return


def dropCobble():
    for i in range(1, 17):
      itemDetail = turtle.getItemDetail(i)
      itemsToDrop = [
          "minecraft:cobblestone",
          "minecraft:gravel",
          "minecraft:andesite",
          "minecraft:diorite",
          "minecraft:granite"
      ]
      if (itemDetail != None):
          if (itemDetail['name'] in itemsToDrop):
              turtle.select(i)
              turtle.dropDown()


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
        