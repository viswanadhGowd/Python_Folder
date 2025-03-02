
"""Open-closed principle (OCP)
OCP : Modules,Classes, methods, Open for extension but closed for modification.
Open for extension means that you should be able to add new functionality to a class or module without changing its existing code
Closed for modification means that the existing code of the class/module should not be altered once it is tested and working.
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, animal: str):
        self.animal=animal

    @abstractmethod
    def get_sound(self):
        pass

class Dog(Animal):
    def __init__(self):
         super().__init__("DOG")

    def get_sound(self):
        return f"{self.animal} Bow Bow!"

class Cat(Animal):
    def __init__(self):
         super().__init__("Cat")

    def get_sound(self):
        return f"{self.animal} Mew Mew!"
    
 
def main():
    print(Cat().get_sound()) #Cat Mew Mew!
    print(Dog().get_sound()) #DOG Bow Bow!

if __name__ == "__main__":
    main()

"""
Output :
Cat Mew Mew!
DOG Bow Bow!

"""