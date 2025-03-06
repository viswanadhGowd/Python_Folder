def Error_handling(test_cases):
    for _ in range(int(test_cases)):
        try:
            a,b=input().split()
            op=int(a)//int(b)
            print(op)
        except ZeroDivisionError as err:
            print(f"Error Code: {err}")
        except ValueError as err:
            print(f"Error Code: {err}")
    
if __name__ == '__main__':
    test_cases = input()    
    Error_handling(test_cases)
    
    # Error_handling("1","0")
    # Error_handling("2","$")
    # Error_handling("3","1")