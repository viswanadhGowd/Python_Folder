"""Single-Responsibility Principle (SRP):
The single-responsibility principle states:
A class should have only one reason to change."""
class Note_Book:
    
    def read(self)-> str:
        return "Note_Book for read"
    
    def write(self)-> str:     
        return "Note_Book for write"

class Laptop:
    
    def typeing(self)-> str:
        return "In laptop we will code"
    
    def watch(self)-> str:
        return "In laptop we will watch videos"

def main():
    note_Book=Note_Book() 
    laptop=Laptop()
    print(note_Book.read()) #Note_Book for read
    print(note_Book.write())  #Note_Book for write
    print(laptop.typeing())#In laptop we will code
    print(laptop.watch()) #In laptop we will watch videos

if __name__ == "__main__":
    main()