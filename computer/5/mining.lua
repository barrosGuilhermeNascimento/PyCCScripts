local miningUtils = require('miningUtils')

for i = 0, 2, 1 do
    turtle.refuel()
    while turtle.getFuelLevel() > 3 do
        for i = 0, 9, 1 do
            miningUtils.digGravel()
            turtle.dig()
            turtle.forward()
            miningUtils.digGravel()
            turtle.digUp()
            miningUtils.digGravel()
            turtle.up()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.down()
        end
        if (miningUtils.findItem("minecraft:torch")) then
            turtle.placeUp()
        end
        turtle.turnRight()
        for i = 0, 4, 1 do
            miningUtils.digGravel()
            turtle.dig()
            turtle.forward()
            miningUtils.digGravel()
            turtle.digUp()       
            turtle.up()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.down()
        end
        turtle.turnLeft()
        turtle.turnLeft()
        for i = 0, 2, 1 do
            turtle.forward()
        end
        turtle.turnLeft()
        for i = 0, 9, 1 do
            miningUtils.digGravel()
            turtle.dig()
            turtle.forward()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.up()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.down()
        end
        if (miningUtils.findItem("minecraft:torch")) then
            turtle.placeUp()
        end
        turtle.turnLeft()
        for i = 0, 2, 1 do
            miningUtils.digGravel()
            turtle.dig()
            turtle.forward()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.up()
            miningUtils.digGravel()
            turtle.digUp()
            turtle.down()
        end
        turtle.turnRight()
        miningUtils.digGravel()
        turtle.dig()
        turtle.forward()
        turtle.digDown()
        miningUtils.DropCobble()
        turtle.turnLeft()
        turtle.turnLeft()
        turtle.forward()
        miningUtils.DropCobble()
    end

end
