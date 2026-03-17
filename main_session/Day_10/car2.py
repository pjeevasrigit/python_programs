from car1 import car

car1=car("Tata punch",2024,"red",False)
car2=car("Celerio",2022,"blue",True)
car3=car("Honda City",2021,"white",True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2.drive()
car3.describe()