"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def my_fun(s):
    temp=[]
    import itertools
    for each in itertools.groupby(s):
        temp.append((len(list(each[1])),int(each[0])))
    print(" ".join([str(x) for x in temp]))
    
    
if __name__ == '__main__':
    STDIN=input()
    my_fun(STDIN)


