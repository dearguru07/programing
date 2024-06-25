# def Printmsg1():
#     print("hello world")
#     printmsg2()

# def printmsg2():
#     print("hello world")
#     printmsg3()

# def printmsg3():
#     print("hello world")
#     printmsg4()

# def printmsg4():
#     print("hello world")
#     printmsg5()

# def printmsg5():
#     print("hello world")
# Printmsg1()

# def Function1(n):
#     if n>5:
#         return
#     print('hello world')
#     Function1(n+1)
# n=1    
# Function1(n)    

# ------------------WAPP to display 1-5:--------------

# def Function2(n):
#     if n>5:
#         return
#     print(n)
#     Function2(n+1)
# n=1
# Function2(n)    
# print('------------')

# ------------------WAPP to display 5-1:--------------

# def Function2(n):
#     if n<1:
#         return
#     print(n)
#     Function2(n-1)
# n=5

# Function2(n)    


# def Pattern(n):
#     if n==1:
#         return '1'
#     else:
#         return str(n) + Pattern(n-1)
# n=5
# print(Pattern(n))    


def Pnum(n,m):
    if n<=m:
        print(n)
        Pnum(n +1,m)
    if n<=m:
        print(n) 
n=1
m=5
Pnum(n,m)
