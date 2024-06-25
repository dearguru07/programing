
# ----------------------leapyear-------------------

# year=int(input("enter a year : "))
# if (year %100!=0 and year%4==0) or (year %400==0):
#     print(year, "is a leap year")
# else:
#     print(year,"is a not leap year")    
    
    
# def CheckYear(year):
#     if (year %100!=0 and year%4==0) or (year %400==0):
#        return True
#     else:
#         return False
# year=int(input('enter a year'))            
# flag=CheckYear(year) 
# if flag==True:
#     print(year,"is leap year")  
# else:
#     print(year,'not a leap year')     


# def CheckYear(year):
#     if (year %100!=0 and year%4==0) or (year %400==0):
#        return True
#     else:
#         return False
# yearsrt=int(input('enter a year'))            
# yearend=int(input('enter a year')) 
           
# if yearsrt>yearend:
#     print('inavalid range')
# else:
#     for i in range(yearsrt,yearend+1):
#       flag=CheckYear(year) 
#       if flag==True:
#         print(year)
              

# n1=int(input('enter a number '))
# n2=int(input('enter a number'))

# if n1>n2:
#     n1,n2=n2,n1
# for i in range(1,n1+1):
#     if (n1%i ==0) and (n2%i ==0):
#         hcf=i
# print(hcf)


def FindHcf(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    for i in range(1,n1+1):
        if (n1% i==0) and (n2%i ==0):
            hcf=i
    return hcf  
        
n1=int(input('enter a number '))
n2=int(input('enter a number'))
result=FindHcf(n1,n2)
print(result)    

# write a python progrsm  to disply LCM(least common mutliplers) of thee given two nbrs 