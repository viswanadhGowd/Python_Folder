"""
interface segregation principle (ISP):
Clients should not be forced to depend on methods they do not use.
Interfaces belong to clients, not to hierarchies.
"""
from abc import ABC, abstractmethod

class SWIM(ABC):

    @abstractmethod
    def can_swim(self):
        pass

class FLY(ABC):

    @abstractmethod
    def can_fly(self):
        pass

class WALK(ABC):
    
    @abstractmethod
    def can_walk(self):
        pass

class FROG(SWIM, WALK):
    
    def __init__(self,name):
        self.name=name
    def can_swim(self):
        return f"{self.name} can swim"
    def can_walk(self):
        return f"{self.name} can walk"
    
class DUCK(SWIM, FLY,):
    def __init__(self,name):
        self.name=name
    def can_swim(self):
        return f"{self.name} can swim"
    def can_walk(self):
        return f"{self.name} can walk"
    def can_fly(self):
        return f"{self.name} can fly"
def main():
    f=FROG("frog")
    print(f.can_swim())
    print(f.can_walk())
    d=DUCK("duck")
    print(d.can_swim())
    print(d.can_walk())
    print(d.can_fly())

if __name__ =="__main__":
    main()

"""
Output:
frog can swim
frog can walk
duck can swim
duck can walk
duck can fly
"""