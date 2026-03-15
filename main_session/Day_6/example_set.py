from main_session.Day_6.example_list import fruits

vegie = {"carrot","radish","beans","potato","cabbage"}

print(vegie)
#{'radish', 'potato', 'beans', 'carrot', 'cabbage'}
#{'potato', 'radish', 'carrot', 'cabbage', 'beans'}

print(len(vegie))

print("radish" in vegie)

#print(vegie[0])

vegie.add("chilly")

print(vegie)

vegie.remove("radish")
print(vegie)

vegie.pop()
print(vegie)

#vegie.clear()
#print(vegie)

print(type(fruits))