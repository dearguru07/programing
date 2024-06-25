# for i in range(5,1,5):
#     print(i)
    
   
# n=int(input('enter'))
# m=int(input('enter '))
# while 
# if n>m:
#     print('inavalid rnage')
# else:
#     a=n+1
#     print(a)       

    
# float=True
# n=int(input('enter a nub'))
# endvalue=n//2
# for i in range(2,endvalue+1):
#     if n% i==0:
#         float=True
#         break
# if float==True and n>1:
#     print('prime')
# else:
#     print('not a prime')        

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.__model = model  # Private attribute
    
#     def get_model(self):
#         return self.__model
    
#     def set_model(self, model):
#         self.__model = model

# my_car = Car("Toyota", "Corolla")
# print(my_car.make)       # Accessible
# print(my_car.get_model()) # Accessing private attribute via getter method

# str="hello"
# str2="world"
# n3=str+str2
# print(n3)


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
