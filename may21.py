# # n=int(input("enter a num:"))
# -------------------reverse Numbers  using Functione-------------

# def reversedigit(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input("enter a num:"))
# res=reversedigit(n)
# print(res)

# -------------------using Functions and range-------------

# def reverse(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# sr=int(input("enter a num:"))
# er=int(input("enter a num:"))
# if sr>er:
#     print("invalid range")
# else:
#     for i in range(sr,er+1):
#         res=reverse(i)
#         print(res)


# --------------------palindrome-----------------

n=int(input("enter a nbr "))
temp=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10 +rem
    n//=10
    # print(n)
if temp==rev:
    print('Polindromme')
else:
    print("Not a Palindrome")


# --------------------using Functions---------------

def Reverse(number):
    rev=0
    while number!=0:
        rem=number%10
        rev=rev*10 +rem
        number//=10
    return rev
n= int(input("enter a number "))
res=Reverse(n)
if n==res:
    print("Palindrome")
else:
    print("not a palindrome")



def Reverse(number):
    rev = 0
    while number != 0:
        rem = number % 10
        rev = rev * 10 + rem
        number //= 10
    return rev
sr = int(input("enter a number "))
er = int(input("enter a number "))
if sr > er:
    print("invalid range")
else:
    for i in range(sr, er + 1):
        res = Reverse(i)
        if i == res:
            print(i)

            