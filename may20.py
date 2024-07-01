#-----------------using Functions for finding the Prime Numbers------------

def checkPrime(n):
    er = n // 2
    for i in range(2, er + 1):
        if n % i == 0:
            return False
    return True


sr = int(input("enter a num"))
er = int(input("enter a num"))

for i in range(sr, er + 1):
    if i > 1:
        flag= checkPrime(i)
        if flag==True:
            print(i)


#-----------------using Functions for finding the Prime Numbers using range------------


# def checkPrime(n):
#     er = n // 2
#     for i in range(2, er + 1):
#         if n % i == 0:
#             return False
#     return True

# sr = int(input("enter a num"))
# er = int(input("enter a num"))
# if sr > er:
#     print("invalid range")
# else:
#     for i in range(sr, er + 1):
#         if i > 1:
#             flag = checkPrime(i)
#             if flag == True:
#                 print(i)


# ----------------counting the digits of the nbrs-----------

# n=int(input("enrter a nub"))
# count=0

# while n>0:
#     n=n//10
#     count=count+1
# print(count)



# def Count(n):
#     Count=0
#     while n>0:
#      n=n//10
#      Count=Count+1
#     return Count
# sr=int(input("entr a number"))
# er=int(input("entr a number"))
# if sr>er:
#     print('invalid range')
# else:
#     for i in range(sr,er+1):
#       results=Count(i)
#       print(i," digit count is ",results)       


