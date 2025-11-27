#Get instance count.
class myclass:
    count=0
    def __init__(self):
        myclass.count+=1

myclass()
myclass()
myclass()
myclass()
print(f"Here the count is {myclass.count}")

class Andhra:
    def __init__(self, name):
        self.name=name
    def capital(self):
        print(f"{self.name} capital is Amaravathi")
    
class Telangalna:
    def __init__(self, name):
        self.name=name
    def capital(self):
        print(f"{self.name} capital is Hyderabad")

def main():
    a=Andhra("Andhra")
    t= Telangalna("telangana")
    a.capital()
    t.capital()

# main()
def wrapper(func):
    def fibo(no):
        n1=0
        n2=1
        for _ in range(no):
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
        return n1
    return fibo

@wrapper
def add(no):
    return no


def remove_duplicates():
    import copy
    l1= [1,3,44,6,64,6,3,1,54,6]
    l2=[y for x,y in enumerate(l1) if y not in l1[:x]]
    print(l2)
    l1.append([94,23,4])
    print(id(l1[-1]))
    l2=l1[:][-1]
    print(id(l2))
    l3=copy.copy(l1)
    print(id(l3[-1]))
    l4=copy.deepcopy(l3)
    l4[-1].append(89)
    print(id(l4[-1]))
    print("---------------")
    print(id(l1))
    l2=l1[:]
    print(id(l2))
    l3=copy.copy(l1)
    print(id(l3))
    l4=copy.deepcopy(l3)
    print(id(l4))
remove_duplicates()

