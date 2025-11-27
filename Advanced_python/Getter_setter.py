class Myclass:
    def __init__(self,no):
        self.__no=no

    def get_a(self):
        return self.__no

    def set_a(self, no):
        self.__no=no
        return self.__no
    
# obj=Myclass(9)
# obj.set_a(12)
# print(obj.get_a())


class Newclass:
    def __init__(self, no):
        self.__no=no

    @property
    def a(self):
        return self.__no

    @a.setter
    def a(self, no):
        self.__no = no+10

# n=Newclass(80)
# print(n.a)
# n.a=5

# print(n.a)


class Another_way:

    def __init__(self,no):
        self.set_data(no)

    def get_data(self):
        return self.__no

    def set_data(self, val):
        self.__no= val+100
        # return self.__no
    
    aa=property(get_data, set_data)

a=Another_way(10)
# print(dir(a))
# print(a.aa)
# print("--exit--")
# import sys; sys.exit()

def check(x,*y):
    print(x, *y)

# check("hi",*[3,5,6,7])


def verify(**kwargs):
    print(kwargs)
    for x, y in kwargs.items():
        print(x,y)

# verify(a=10, b=20, c=90)

def reverse():
    n=8972
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
# reverse()

x = 0
def fncn():
    global x
    x = x+1
    print(x)
    return fncn()

# fncn()

def mask_card(st):
    n=""
    count=0
    for each in range(3,len(st), 3):
        newst=st[count: each+1]
        count=each
        temp=newst[0]+"*"+newst[2::]+" "
        n+=temp
    print(n)
# mask_card(st="1234567809876543")

def pagenation(page, num, data):
    inx=(page-1)* num
    print(data[inx: inx+num])

# pagenation(4,10, [x for x in range(1,100)])


l=[45,6,4,63,67,34,4,5,5]
l2=[]
def my_min_sort(l):
    min_val=l[0]
    for each in l:
        if each < min_val:
            min_val=each
    l2.append(min_val)
    l.remove(min_val)
    if len(l)>1:
        my_min_sort(l)
# my_min_sort(l)

def swaping(l):
    for i in range(len(l)):
        min_val=i
        for j in range(i+1,len(l)):
           if l[j]<l[min_val]:
               min_val=j
        print(l[min_val])
        l[i],l[min_val]= l[min_val], l[i]
    print(l)
# swaping(l)



l1=[2,8,1,5,7] #[7, 5, 1, 8, 2]
def reverse_list(l):
    l2=[l1[x] for x in range(len(l)-1,-1,-1)]
    print(l2)
reverse_list(l1)

l1=[2,8,1,5,7,[78,4,6,[5,3,5]]]
l2=[]
def flated_list(l):
    for each in l:
        if isinstance(each, int):
            l2.append(each)
        else:
            flated_list(each)
flated_list(l1)
print(l2)