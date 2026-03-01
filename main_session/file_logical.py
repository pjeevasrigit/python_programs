### AND OR NOT

temp = 25
is_raining = False

if temp > 35 or is_raining:
    print ("Climate is Hot")
elif temp < 10 and is_raining:
    print ("It is too cold")
elif not is_raining:
    print ("It is not raining")
else:
    print("Stay safe")