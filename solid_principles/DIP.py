"""
Dependency inversion principle (DIP):
Abstractions should not depend upon details. Details should depend upon abstractions.
"""
from abc import ABC, abstractmethod

class Human:
    def __init__(self, feed_type:object):
        self.feed_type=feed_type
    def display_feed(self):
        return f"A human can {self.feed_type.feed()}"

class Displayfeed(ABC):
    @abstractmethod
    def feed(self):
        pass

class Food(Displayfeed):
    def feed(self):
        return "have a food" 

class Drink(Displayfeed):
    def feed(self):
        return "have a water" 

def main():

    for each in [Human(Food()),Human(Drink())]:
         print(each.display_feed())

if __name__ == "__main__":
    main()

"""
Output: 
A human can have a food
A human can have a water

"""