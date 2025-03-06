"""
Itertools, Maximize It code:
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def iter_max(arg):
    K,M=arg.split()
    temp=[]
    L = [list(map(int, input().split()))[1:] for i in range(int(K))]
    result = 0
    for i in itertools.product(*L):
        count = 0
        for n in i:
            count += n**2
            
        if result < count % int(M):
            result = count % int(M)
    print(result)
    
            

if __name__ =="__main__":
    t1=input()
    iter_max(t1)
    


# t1=input()
# t2=input()
# t3=input()
# t4=input()

# print(t1)
# print(t2)
# print(t3)
# print(t4)
