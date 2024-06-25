# ---------------LCM-----------------

# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))

# if num1>num2:
#     num1,num2=num2,num1

# lcm=num2

# while True:
#     if lcm%num1==0 and lcm%num2==0:
#         break
#     lcm+=num2
# print('the lcm of given number is',lcm)

# ---------------Using Functions------------

# def LCM(num1, num2):
#     if num1 > num2:
#         num1, num2 = num2, num1

#     lcm = num2
#     while True:
#         if lcm % num1 == 0 and lcm % num2 == 0:
#             break
#         lcm += num2
#     return lcm


# num1 = int(input("enter a number:"))
# num2 = int(input("enter a number:"))
# result = LCM(num1, num2)
# print("The lcm of given numbers is", result)


# ----------------------Fibonacci  numbers-------------


n=int(input('enter a number '))
n1=0
n2=1
for i in range(1,n+1):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3

# --------------------using Functions---------------


def Fibnocci(n):
    n1 = int(input("enter first number"))
    n2 = int(input("enter second number"))
    if n1 > n2:
        print("Please enter valid range")
    else:
        for i in range(1, n + 1):
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            
n = int(input("enter a number "))
Fibnocci(n)
