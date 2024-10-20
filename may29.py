# def Function(n):
#     if n > 5:
#         return
#     print(n)
#     Function(n + 1)
#     print(n)
#     return
# n = 1
# Function(n)

# --------------sum of the first N natural Numbers----------

def Sum(n):
    if n==1:
        return n
    return n+Sum(n-1)
n=int(input("enter a number"))
totalSum=Sum(n)
print(totalSum)

# --------------product of the first N natural Numbers----------

# def Product(n):
#     if n==1:
#         return n
#     return n*Product(n-1)
# n=int(input("enter a number"))
# res=Product(n)
# print(res)

# -----------counting the digits in give nember using recursion---------------

# def CountDigit(n,count):
#     if n==0:
#         return count
#     n=n//10
#     count+=1
#     return CountDigit(n,count)

# n=int(input('enter a number'))    
# res=CountDigit(n,0)
# print(res)

print('Hello world......')