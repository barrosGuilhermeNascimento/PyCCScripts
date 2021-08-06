
function findItem(item)
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

while true do
    local okay, inspect = turtle.inspect()
    if (inspect.state.age == 7) then
        turtle.dig()
        findItem("minecraft:wheat_seeds")
        turtle.place()
    else
        findItem("minecraft:bone_meal")
        turtle.place()
    end

end
