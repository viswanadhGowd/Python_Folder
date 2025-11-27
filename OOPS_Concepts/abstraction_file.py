from abc import ABC, abstractmethod

class Base_subject(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def get_subject_name(self):
        pass 

class subject(Base_subject):
    def __init__(self,name):
        self.name=name
    def get_subject_name(self):
        return self.name

class teacher:
    
    def __init__(self,name,subject_name):
        self.name=name
        self.subject=subject(subject_name)
        
    def get_info(self):
        print(f"The teacher name is {self.name} and subject is {self.subject.get_subject_name()}")


def main():
    t=teacher("Viswanadh", "computer science")
    t.get_info()

if __name__=="__main__":
    main()
#test