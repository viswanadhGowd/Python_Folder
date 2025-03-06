"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

def list_methods(N):
    temp=[]
    for _ in range(N):
        str_ip=input()
        command=str_ip.split()[0]
        if command in ("insert"):
            inx=str_ip.split()[1]
            val=str_ip.split()[2]
            temp.insert(int(inx),int(val))
        elif command in ("print"):
            print(temp)
        elif command in ("remove"):
            temp.remove(int(str_ip.split()[-1]))
        elif command in ("append"):
            temp.append(int(str_ip.split()[-1]))
        elif command in ("sort"):
            temp.sort()
        elif command in ("pop"):
            temp.pop()
        elif command in ("reverse"):
            temp.reverse()
        
    
if __name__ == '__main__':
    N = int(input())
    list_methods(N)
    