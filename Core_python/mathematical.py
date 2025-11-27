# for each in range(1,40):
#     if each%2==0:
#         print(each,"----",True)
#     else:
#         print(each,"----",False)

# def prime(no):
#     for x  in range(2, no):
#         if no%x==0:
#             break
#     else:
#         print(f" {no} It's a prime number")
# for each in range(2, 20):
#     prime(each)


# def composite(no):
#     for x in range(2,no):
#         if no%x==0:
#             print(f"{no} its a composite number")
#             break
#         else:
#             pass
# for y in range(2,20):
#     composite(y)

def different_copy():
    import copy
    actual_list=[23,4,[45,98]]
    copied_list=copy.deepcopy(actual_list)
    copied_list[2][0]=96
    print(actual_list, id(actual_list))
    print(copied_list, id(copied_list))
    

different_copy()
