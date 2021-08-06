#from computercraft.subapis import turtle, gps, import_file
from cc import turtle, gps, import_file
utils = import_file('miningUtils.py', __file__)  # relative to current file
#from .miningUtils import findItem, digGravel

beginLocation : list
beginLocation = []

def dig():
#    move("forward", 2, "left", turtle.dig, turtle.digUp)
    utils.digGravel()
    turtle.dig()
    turtle.forward()
    utils.digGravel()
    turtle.digUp()
    turtle.up()
    utils.digGravel()
    turtle.digUp()
    turtle.down()

while True:
    beginLocation.append({'x': gps.locate()[0], 'y': gps.locate()[1], 'z': gps.locate()[2]})

    for i in range(10):
        dig()
    if(utils.findItem("minecraft:torch")):
        turtle.placeUp()
    turtle.turnRight()
    for i in range(6):
        dig()
    turtle.turnRight()
    turtle.turnRight()
    utils.move("forward", 3)
    turtle.turnLeft()
    for i in range(10):
        dig()
    if(utils.findItem("minecraft:torch")):
        turtle.placeUp()
    turtle.turnLeft()
    for i in range(3):
        dig()
    turtle.turnRight()
    turtle.dig()
    turtle.forward()
    turtle.digDown()
    utils.dropCobble()
    turtle.turnLeft()    
    turtle.turnLeft()
    turtle.forward()
