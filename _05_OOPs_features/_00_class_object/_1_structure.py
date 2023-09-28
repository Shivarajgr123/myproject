# Everything is an object in Python

x = 10  # int(10) # object creation
x = int(10)

str1 = "Madhu"  # str("Madhu")
str1 = str("Madhu")
str1.lower()

list1 = [1, 2, 3]
list1 = list([1, 2, 3])
list1.pop()

# EVERYTHING IS AN OBJECT IN PYTHON

'''
Student
------------
 IV : r_no name   marks   percentage   section   fee    student_address
 CV : school_name school_address student_count
 

Instance variable : Individual to each object
Class variable    : Sharable and modifiable by all objects


CV  ----> CM  Yes
IV  ----> IM  Yes

CV  ----> IM  Yes
IV  ----> CM  No

'''
'''
CLASS:
============
    STATE 
     - Fields
        - Class variables 
        - Instance variables 
      
    BEHAVIOR
     - Methods
        - Class method
        - Instance method
        - Static method
    
STATE  - BEHAVIOR
Fields - Methods

OOPs concepts:
--------------------
Class Object
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

1. Encapsulation: Binding Data Members and Member Methods into Single entity.

2. Inheritance :
---------------
super class, sub class mechanism


3. Polymorphism :
---------------
    - Static Polymorphism  -- Method overloading ***
    - Dynamic Polymorphism -- Method overriding  ***

4. Abstraction   : 
----------------------
Hiding implementation details and exposing only method signature 

Abstraction   :      Class          -  0% abstraction
                     Abstract class -  0% to 100% abstraction
                     Interface      - 100%  abstraction 
class,object

Hiding the implementation details in the methods of  a class

In a "Normal class" Abstraction is 0%        # all concrete methods
In "Abstract Class" Abstraction is 0-100 %   # 1. all concrete methods,
                                               2. all abstract methods
                                               3. Comb of concrete+abstract methods
In an "Interface"   Abstraction is 100%      # all abstract methods


'''

'''
 1. Class Defined and provided special method i.e, 
   __init__(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         Python creates empty object for us,and gives reference to self parameter
         Reamining parameters, we are passing the arguments
         In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS
4. We can perform method calls using created object       
'''



