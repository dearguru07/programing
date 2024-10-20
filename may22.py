# <<----------------Armstrong Numbers------------------->>

def CountOfDigit(n):
    Count=0
    while n!=0:
        n=n//10
        Count+=1
    return Count    
def checkA(n):
    temp=n
    sum=0
    pow=CountOfDigit(n)
    while n!=0:
        rem=n%10
        sum=sum+rem**pow
        n=n//10
    if temp==sum:
        return True
    else:
        return False
n=int(input("eter a nmb"))
flag=checkA(n)
if flag==True:
    print('nbr is Am')
else:
   print('not ams')




# def CountOfDigit(n):
#     Count=0
#     while n!=0:
#         n=n//10
#         Count+=1
#     return Count    
# def checkA(n):
#     temp=n
#     sum=0
#     pow=CountOfDigit(n)
#     while n!=0:
#         rem=n%10
#         sum=sum+rem**pow
#         n=n//10
#     if temp==sum:
#         return True
#     else:
#         return False
# sr=int(input("eter a nmb"))
# er=int(input("eter a nmb"))
# if sr > er:
#     print("invalid range")
# else:
#     for i in range(sr, er + 1):
#         flag=checkA(i)
#         if flag==True:
#             print(i , "is a AmsN")
#         # else :
#         #    print(i,'not a AMs')  

#  ------------------numerical programs in google------------->>