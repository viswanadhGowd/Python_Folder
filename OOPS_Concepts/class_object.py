
class sample:
    def __init__(self, no1):
        self.no1=no1
    def add(self):
        return f"After adding no 10 to {self.no1+10}"

def main():
    s=sample(10) #  here "s" is the object reference variale for sample(10) 
    print(s.add())

if __name__ == "__main__":
    main()