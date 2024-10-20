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


# def Polyn(n):
#     rev=0
#     tem=True
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n= int(input('entr a num'))
# res=Polyn(n)
# if n==res:
#     print('polyn')
# else:
#     print('not')        


# def Reverse(n):
#     rev=0
#     while n!=0:
#         rem=n %10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('enter a nub'))    
# res=Reverse(n)
# print(res)



# ---------------String Reversal (increment loop)----------------------

# def NewR(strN):
#     newSTRR=""
#     for i in range(0,len(strN)):
#         newSTRR=strN[i]+newSTRR
#     return newSTRR
# strN=input("enter a nuw str")
# resul=NewR(strN)
# print(resul)



# reversed sentance---------------

# def Reversal_loop(nstr, i, s1):
#     if i == len(s1):
#         return nstr
#     nstr = s1[i] + nstr
#     return Reversal_loop(nstr, i + 1, s1)
# s1 = input("enter a new string : ")
# result = Reversal_loop("", 0, s1)
# print(result)


# ---------------String Reversal (recursion) --------------


def Reverse(n):
    str=''
    for i in n:
        str=i+str
    return str
n=str(input('enter a string'))    
Reversed=Reverse(n)
print(Reversed)
if n==Reversed:
    print('polyndrome')
else:
    print('not a polyndrm')

# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character in vowel:
#         count += 1
# print(count)


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character not in vowel:
#         count += 1
# print(count)


# max number finding-------------

# numberList = [15, 85, 35, 89, 125]

# maxNum = numberList[0]
# for num in numberList:
#     if maxNum < num:
#         maxNum = num
# print(maxNum)


# min number finding------------

# numberList = [15, 85, 35, 89, 125, 2]

# minNum = numberList[0]
# for num in numberList:
#     if minNum > num:
#         minNum = num
# print(minNum)


# # fing mid ele in list------------

# numList = [1, 2, 3, 4, 5]
# midElement = int((len(numList)/2)) 

# print(numList[midElement])


# # Anagrams or not-------------------

str1 = str(input('enter a str'))
str2 = str(input('enter a str'))

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")
