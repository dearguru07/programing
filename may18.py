

# flat = True
# n = int(input("enter a num "))
# endrange = n // 2
# for i in range(2, endrange + 1):
#     if n % i == 0:
#         flat = False
#         break
# if flat == True and n > 1:
#     print("prime")
# else:
#     print("not a prime")


# def PrintMsg():
#     print("Function exc")
#     # return
# print("prgm srtd")
# PrintMsg()
# print('prgm end')    


def Prime(n):
    tem=True
    en=n//2
    for i in range(2,en+1):
        if n%i==0:
            tem=False
            break
    if tem==True and n>1:
        print('prime')    
    else:
        print('not a prime')    
n=int(input('enter a number'))        
Prime(n)