# class addition:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
    
#     def add(self):
#         print(f"here {self.n2}")
#         return self.n1+10

# class substraction:
#     def __init__(self,no1):
#         self.n1=no1
    
#     def sub(self):
#         return self.n1-10

# class math(substraction, addition):
#     def __init__(self, no1,no2):
#         addition.__init__(self,no1,no2)
#         substraction.__init__(self,no1)

# def main():
#     m=math(100,11)
#     print(m.sub())
#     print(m.add())

# main()
import gc
class addition:
    def __init__(self,no1=None ,no2=None,**kwargs):
       
        # super().__init__(**kwargs)
        self.n1=no1
        self.n2=no2
    
    def add(self):
        print(f"here {self.n2}")
        return self.n1+10

class substraction:
    def __init__(self,no1=None,**kwargs):
        super().__init__(**kwargs)
        self.n1=no1
    
    def sub(self):
        return self.n1-10

class math(substraction, addition):
    def __init__(self,no1,no2):
        super().__init__(no1=no1, no2=no2)

def main():
    m=math(100,11)
    print(m.sub())
    print(m.add())


import gc
def solve():
    st="aabbbcddeeff"
    count=1
    t=""
    for inx in range(1, len(st)):
        if st[inx-1]==st[inx]:
            count+=1
        else:
            t+=st[inx-1]+str(count)
            count=1
    else:
        t+=st[inx-1]+str(count)
    print(t)

def solve1():
    s="a2b3c1d2e2f2"
    e=""
    for each in range(0,len(s),2):
        t=int(s[each+1])
        e+=s[each]*t
    print(e)
# solve1()
def test_counter():
    st="hello world how are you"
    a="aeiou"
    l=list(a)
    vowels=0
    const=0
    for each in list(st):
        if each !=" ":
            if each in l:
                vowels+=1
            else:
                const+=1
    print(vowels,const)
# test_counter()
def prime(no):
    if no == 2:
        return True
    else:
        for each in range(2,no):
            if no%each==0:
                return True
        else:
            return False

# for x in range(2,40):
#     if prime(x)==False:
#         print(x)

def fibo(no):
    n1=0
    n2=1
    for each in range(no):
        nth=n1+n2
        n1=n2
        n2=nth
    print(n1)    
# fibo(15)

def sorting():
    l=[4,5,2,1,3,13]
    m=l[0]
    for each in l:
        if each < m:
            m=each
    print(m)
# sorting()

def temp():
    f = open("Advanced_python/temp.txt", "r")
    f.seek(3)
    print(f.tell())
    print(f.readlines())
    f.close()

def temp1():
    with open("Advanced_python/temp.txt", "r") as ro:
        data=ro.readlines()
        print(data)

# temp1()
def temp2():
    l1=lambda x: x.get("pop")
    data = [
        {"city": "Bangalore", "pop": 102},
        {"city": "udupi", "pop": 99},
        {"city": "Manglore", "pop": 106},
        {"city": "Ballary", "pop": 44},
    ]
    data.sort(key=l1, reverse= True)
    print(data)
# temp2()

def temp3():
    ip = "aaabbccab"
    output = "a3b2c2a1b1"
    count=1
    temp=""
    for inx in range(1,len(ip)):
        if ip[inx-1]==ip[inx]:
            count+=1
        else:
            temp=temp+ip[inx-1]+str(count)
            count=1
    else:
        temp=temp+ip[inx]+str(count)
    print(temp)
# temp3()
def temp4():
    st="likith was born on 1-11-2000"
    import re
    pattern=r"\d{1,2}-\d{1,2}-\d{1,4}"
    # p= r"\d{1,2}-\d{1,2}-\d{4}"
    p=r"\s\w{1,4}"
    st="viswa134.g@gmail.com3"
    p=r"^[a-zA-Z0-9$.]+@[a-zA-Z]+\.[a-z]{2,3}$"
    d=re.search(p, st)
    if d:
        print(d.group())
# temp4()

def temp5():
    l=[1,2,3,4,[], 5, []]
    l2=[x for x in l if isinstance(x,int)]
    d={x:x+1 for x in l if isinstance(x,int)}
    print(d)
    print(l2)
# temp5()

def reverse_no():
    no=2354
    rev=0
    while no>0:
        d=no%10
        rev=rev*10+d
        no=no//10
    print(rev)

# reverse_no()
def temp6():
    output = []
    inout = {"Manoj Test": 12345, "chandra hasa":3452}
    for key,value in inout.items():
        names = key.split()
        names_i = "".join([i[0] for i in names])
        odd = sum([int(i) for i in str(value) if int(i) % 2 != 0])
        output.append(f'{names_i}{odd}')

    print(output)

# temp6()
def temp7():
    d = {}
    d["a"] = d
    d["a"]['b'] = 100
    print(d)#{"a":{"b":100}}
temp7()

