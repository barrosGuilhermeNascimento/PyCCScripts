local UTILSFUNCS=...
local utils = {}


function utils.digBlock(blockName) 
    local levels = 0
    local runned = false
    local returnInspect, information = turtle.inspect()
    if (returnInspect == false) then
        return runned
    end
    while true do
        if (information.name == blockName) then
            runned = true
            turtle.digUp()
            turtle.up()
            levels = levels + 1
        elseif (levels > 0) then
            while (levels > 0) do
                turtle.down()
                turtle.dig()
                levels = levels - 1
            end
            levels = 0
        elseif (levels == 0) then
            return runned
        end

        returnInspect, information = turtle.inspect()
    end   
end

function utils.findItem(item)
    for i = 1, 16, 1 do
        local itemDetail = turtle.getItemDetail(i)
        if (itemDetail ~= nil) then
        if (itemDetail.name == item) then
            turtle.select(i)
            return true
        end
        end
    end
end

function utils.storeItems()
    local onePack = false
    for i = 1, 16, 1 do
        local itemDetail = turtle.getItemDetail(i)
        if (itemDetail ~= nil) then
            if(itemDetail.name == "minecraft:oak_sapling") then
                if (onePack) then
                    turtle.select(i)
                    turtle.drop()
                else
                    onePack = true
                end
            else
                turtle.select(i)
                turtle.drop()
            end
        end
    end
end

function utils.findOcurrences(blockname)
  local previousSelection = turtle.getSelectedSlot()
  local occurrences = {}
  for i = 1, 16, 1 do
    -- turtle.select(i)
    if turtle.getItemDetail(i) ~= nil then
      if turtle.getItemDetail(i).name == blockname then
        table.insert(occurrences, i)
      end
    end
  end

  turtle.select(previousSelection)
  print('na func')
  print(textutils.serialize(occurrences))
  print('depois da func')
  return occurrences
end

function utils.findTotalCount(blockname)
  local previousSelection = turtle.getSelectedSlot()
  local count = 0
  for i = 1, 16, 1 do
    -- turtle.select(i)
    if turtle.getItemDetail(i) ~= nil then
      if turtle.getItemDetail(i).name == blockname then
        count = count + turtle.getItemDetail().count
      end
    end
  end
  turtle.select(previousSelection)
  return count
end

function utils.forward(distance)
  for i = 1, 10, 1 do
    
  end
end
  
return utils