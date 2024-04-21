def test():   
    a="Hello world"
    print(a)
    l1=a.split(" ")
    print(l1)
    l2=a.strip("H")
    l3=l2.lstrip("e")
    l3=l3.rstrip("d")
    l3=l3.rsplit("l")
    print(l3)
# test()

def fact(num):
    factorial=1
    for each in range(1,num+1):
        factorial=factorial*each
    print(factorial)

fact(num=7)

def prime_no(num):
    if num >1:
        for each in range(2,num):
            pass            
prime_no(0)
