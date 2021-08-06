local mininUtilsFuncs=...
local miningUtils = {}

function isIn(table, string)
    local index={}
    for k,v in pairs(table) do
        index[v]=k
    end
    local returnIndex = index[string]
    if (returnIndex ~= nil) then
        if ( returnIndex > 0) then
            return true
        else 
            return false
        end
    end
    return false
  end

function miningUtils.refuelMiner()
    if (turtle.getFuelLevel() < 10) then
        if (miningUtils.findItem("minecraft:coal")) then
            turtle.refuel()
        end
    end
end

function miningUtils.findItem(item)
    for i = 1, 16, 1 do
        local itemDetail = turtle.getItemDetail(i)
        if (itemDetail ~= nil) then
            if (itemDetail.name == item) then
                turtle.select(i)
                return true
            end
        else
            return false
        end
    end    
    return false
end

function miningUtils.digGravel() 
    local levels = 0
    local returnInspect, information = turtle.inspect()
    if (information.name == nil) then
        return
    end
    if (information.name == "minecraft:gravel") then
        turtle.digUp()
        turtle.up()
        levels = levels + 1
    elseif (levels > 0) then
        for i = levels, 0, -1 do
            turtle.dig()
            turtle.down()
        end
        levels = 0
    end
    return
end

function miningUtils.DropCobble()
    for i = 1, 16, 1 do
      local itemDetail = turtle.getItemDetail(i)
      local itemsToDrop = {
          "minecraft:cobblestone",
          "minecraft:gravel",
          "minecraft:andesite",
          "minecraft:diorite",
          "minecraft:granite"
      }
      if (itemDetail ~= nil) then
          if (isIn(itemsToDrop, itemDetail.name)) then
              turtle.select(i)
              turtle.dropDown(itemDetail.count)
          end
      end  
    end
  end

return miningUtils