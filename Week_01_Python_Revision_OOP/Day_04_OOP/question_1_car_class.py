# Create a Car class with attributes (brand, model, year) and a method that displays the car’s info.

class Car:
    def __init__(self, brand, model ,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def car_info(self):
        print(f"Car brand is {self.brand}, model is {self.model} and year is {self.year}")

car = Car("Toyoto", "Revo", 2024)
car.car_info()

