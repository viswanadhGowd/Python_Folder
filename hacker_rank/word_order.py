"""
Word order

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def occurence_words(arg):
    d={}
    for _ in range(arg):
        ip=(input())
        val=d.get(ip)
        if val:
            temp=val+1
            d[ip]=temp
        else:
            d[ip]=1
    
    op=[str(each) for each in d.values()]
    print(len(op))
    # print(op)
    print(" ".join(op))

if __name__=="__main__":
    occurence_words(int(input()))
    
    