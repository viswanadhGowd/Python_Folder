"""
Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.
Sample Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output:
4
Explanation
The roll numbers of students who only have English newspaper subscriptions are:
 and .
Hence, the total is  students.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_number_students(arg1,arg2):
    if int(arg1)< 1000:
        set_data=set(arg2.split())
        return set_data
    
if __name__ == "__main__":
    ip1=input()
    ip2=input()
    english=get_number_students(ip1,ip2)
    ip3=input()
    ip4=input()
    frech=get_number_students(ip3,ip4)
    op=english-frech
    print(len(op))