object = {}
object.gender = 'f'
object.age = 18

print(object)
print(object.gender)
print(object.age)

for i,v in pairs(object) do
    print(i,v)
end


array = {1,2,3,4,5}

for i, v in pairs(array) do
    print(i,v)
end


table.insert(array, 10)

table.foreach(array, function(i, v)
    print(i, v)
end)