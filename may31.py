# def Reverse(n,sum):
#     if n==0:
#         return sum
#     rem=n%10
#     sum=sum*10+rem
#     return Reverse(n//10,sum)
# n=int(input('enter a number '))
# res=Reverse(n,0)
# print(res)
# if n==res:
#     print("polindrome")
# else:
#     print('not a polindrome') 
    
    
def CountDig(n,count):
    if n==0:
        return count
    return CountDig(n//10,count+1)
def SumASN(n,sum,pow):
    if n==0:
        return sum
    rem=n%10
    sum=sum+rem**pow
    return SumASN(n//10,sum,pow)
n=int(input('enter a number'))
count=CountDig(n,0)
res=SumASN(n,0,count)
if n==res:
    print("ASN")
else:
    print("not a ASN")      



# def fib(pos,n1,n2):
#     if pos==0:
#         return
#     print(n1)
#     fib((pos-1),n2,(n1+n2))
# pos=int(input("enter a value"))
# res=fib(pos,0,1)    
# print(res)

