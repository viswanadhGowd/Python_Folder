
"""Open-closed principle (OCP)
OCP : Modules,Classes, methods, Open for extension but closed for modification.
Open for extension means that you should be able to add new functionality to a class or module without changing its existing code
Closed for modification means that the existing code of the class/module should not be altered once it is tested and working.
"""
from abc import ABC, abstractmethod

class Millage(ABC):

    def __init__(self, vehicle: str):
        self.vehicale=vehicle

    @abstractmethod
    def get_millage(self):
        pass

class Bus(Millage):
    def __init__(self, fuel_liters):
        self.fuel_liters=fuel_liters
        super().__init__("BUS")

    def get_millage(self):
        return f"the bus filled with {self.fuel_liters} litters oil, The {self.vehicale} approximently Millage will come {self.fuel_liters * 15}"
    
class Bike(Millage):
    def __init__(self, fuel_liters):
        self.fuel_liters=fuel_liters
        super().__init__("Bike")

    def get_millage(self):
        return f"the Bike filled with {self.fuel_liters} litters oil, The {self.vehicale} approximently Millage will come {self.fuel_liters * 65}"

def main():
    vehicle_list=[Bus(10), Bike(5)]
    def fetch_data(vehicle_list):
        for each in vehicle_list:
            print(each.get_millage())
    fetch_data(vehicle_list)

if __name__ == "__main__":
    main()

"""
Output :

the bus filled with 10 litters oil, The BUS approximently Millage will come 150
the Bike filled with 5 litters oil, The Bike approximently Millage will come 325
"""