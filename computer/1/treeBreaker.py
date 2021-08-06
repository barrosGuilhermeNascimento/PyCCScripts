from .utils import

treeLocations = {    
    # first Row
    {'x' : 243, 'z' : -246},
    {'x' : 243, 'z' : -249},
    {'x' : 243, 'z' : -251},
    {'x' : 243, 'z' : -254},
    {'x' : 243, 'z' : -257},
    {'x' : 243, 'z' : -260},
    {'x' : 243, 'z' : -263},

    #  Second Row
    {'x' : 246, 'z' : -246},
    {'x' : 246, 'z' : -249},
    {'x' : 246, 'z' : -251},
    {'x' : 246, 'z' : -254},
    {'x' : 246, 'z' : -257},
    {'x' : 246, 'z' : -260},
    {'x' : 246, 'z' : -263},

    #  Third Row
    {'x' : 249, 'z' : -246},
    {'x' : 249, 'z' : -249},
    {'x' : 249, 'z' : -251},
    {'x' : 249, 'z' : -254},
    {'x' : 249, 'z' : -257},
    {'x' : 249, 'z' : -260},
    {'x' : 249, 'z' : -263},

    #  Fourth Row
    {'x' : 251, 'z' : -246},
    {'x' : 251, 'z' : -249},
    {'x' : 251, 'z' : -251},
    {'x' : 251, 'z' : -254},
    {'x' : 251, 'z' : -257},
    {'x' : 251, 'z' : -260},
    {'x' : 251, 'z' : -263},
}
runnedDig
while true:
    for x = 0, 1, 1 do
        turtle.turnLeft()
        for i = 0, 6, 1 do
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.turnRight()
            runnedDig = utils.digBlock("minecraft:oak_log")
            print(runnedDig)
            if (runnedDig) then
                if(utils.findItem("minecraft:oak_sapling")) then
                    turtle.place()
                end
            end
            turtle.turnLeft()
        end
        for i = 0, 1, 1 do
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.turnRight()  
        end
        for i = 0, 6, 1 do
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.forward()
            turtle.suck()
            turtle.turnLeft()
            runnedDig = utils.digBlock("minecraft:oak_log")
            print(runnedDig)
            if (runnedDig) then
                if(utils.findItem("minecraft:oak_sapling")) then
                    turtle.place()
                end
            end
            turtle.turnRight() 
        end
        turtle.forward()
        turtle.suck()
        turtle.forward()
        turtle.suck()
        turtle.forward()
        turtle.turnLeft()
        turtle.forward()
        turtle.suck()
        turtle.forward()
        turtle.suck()
        turtle.forward()
    end
    turtle.turnLeft()
    turtle.turnLeft()
    for i = 0, 12, 1 do
        turtle.suck()
        turtle.forward()
    end
    #  restore fuel
    if (turtle.getFuelLevel() < 960) then
      turtle.select(utils.findOcurrences('minecraft:oak_log')[1])
      turtle.refuel()
    end
    
    print(textutils.serialize(turtle.getItemDetail()))
    
    #  store items in the Chest
    utils.storeItems()
    turtle.turnLeft()
    turtle.turnLeft()
end
