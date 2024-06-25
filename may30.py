
# def Reverse(n, revnum):
#     if n == 0:
#         return revnum
#     return Reverse(n // 10, revnum * 10 + n % 10)
# num = int(input("enter a number"))
# revnum = Reverse(num,0)
# print(revnum)


def Fib(n):
    n1=0
    n2=1
    if n==0:
        return 0
    num=n+1
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    return Fib(n)
n=int(input('enter a number'))
res=print(num)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input('enter a number : '))  
# result = fibonacci(n)
# print(result)

