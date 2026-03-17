# objects - A bundle of related attributes
# class - blue print, layout
# constructor

class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")
    def describe(self):
        print(f"year is {self.year}, model is {self.model}, color is {self.color}")
