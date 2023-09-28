''''''
'''
Why Abstraction is required ?

SC: Each sub class wants their own body uniquely.

                           Animal
                                eating()    # Why should i provide body here ?
                                   
                  Cat          Dog       Tiger      Lion
                    eating()    eating()  eating()    eating()
'''
from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract class

    @abstractmethod
    def eating(self):   # abstract method : Incomplete method / Method without body
        pass

class Cat(Animal):
    def eating(self):
        print("Cat eating()")

cat = Cat()
cat.eating()



'''
Here all sub classes of Animal,inherits eating() and running() AS IS, 
but sleeping() method is required for all sub classes, at the same time need to be implemeneted uniquely.

'''

'''
An Abstract class can have 
    - All Concrete Methods   : Class 
    - All Abstract Methods   : Interface
    - Combination of Concrete+Abstract Methods : Abstract Class
    
Specification/Contract: 
=========================
class Employee:
    def m1():
        pass
class SoftEmployee(Employee):
    def m2():
        pass
                                                                      Capacity  Content
1. float x = 10.5      Employee emp = Employee()                      5L         5L
2. int   x = 10    SoftEmployee emp = SoftEmployee()                  2L         2L
3. float x = 10        Employee emp = SoftEmployee()* # Upcasting     5L         2L 
4. int x = 10.5    SoftEmployee emp = Employee()      # Downcasting   2L         5L

Employee emp = SoftEmployee()
emp.m1()
emp.m2()  # ERROR



'''

class Animal(ABC):   # Abstract class

    def eating(self):   # concrete method/normal method
        print("Animal eating")

    def running(self):  # concrete method
        print("Animal running")

    @abstractmethod    # abstract method
    def sleeping(self):
        pass

class Cat(Animal):

    def sleeping(self):
        print("Cat sleeping")

cat = Cat()
cat.eating()
cat.running()
cat.sleeping()
