'''
Inheritance : is - a   **: - Triangle is a Polygon
Aggregation : has - a    : - Triangle has 3 sides


 - Employee has eid
 - Employee has name
 - Employee has salary
 - Employee has address


'''
'''
has - a : Aggregation:

Web Application:  
                UI   --->        Python            ----> Database 
                            Controller Service DAO 
'''

class Address:
    def __init__(self, hno, bno, blockno):
        self.hno = hno
        self.bno = bno
        self.blockno = blockno

    def get_address(self):
        return self.hno + " , " + self.bno + " , " + self.blockno


class Employee:
    def __init__(self, eid: int, name: str, sal: float, addr: Address):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.addr = addr  # User Defined Class

    def get_einfo(self):
        print("employee info", self.eid, self.name,self.sal, self.addr.get_address())


address = Address('100', '25', '450')
madhu = Employee(123, 'Madhu Nettem', 15000, address)
madhu.get_einfo()

'''
is - a : Inheritance:
=======================
Parent
Children

Square is a Quadrilateral 

Parent, Base,    Super Class : Quadrilateral
Child,  Derived, Sub Class   : Square 

is-a relationship    <SUB> is a <SUPER>
SoftwareEmployee is a Animal  #Not valid 

2 classes: 
    Super   - Sub* 
    Parent  - Child* 
    Base    - Derived 

madhu = Employee() 
    madhu = Physical 
    Employee = Logical 

Problem:             Tiger    Lion        Cat         Dog 
                     eating()   eating()   eating()    eating()
    
    
Solution:                 Animal
                            eating()
               |      |           |     |
              Tiger  Lion        Cat    Dog       A5 A6 A7 A8 ......


A3:                        Animal
                  |                   |
                Wild               Domestic
                |  |                 |     |
             Tiger Lion              Cat   Dog 
    
    

Without inheritance:
---------------------
Tiger, Lion, Cat, Dog 

A1:    Tiger        Lion              Cat         Dog 
        eating()    eating()           eating()   eating()   
  
  # Code duplication, Maintenance, Enhancements

With inheritance:
---------------------
A2:                   Animal
        Tiger   Lion         Cat    Dog 
    
                       Animal
                         eating()         # code reusability, avoids code duplication
             |        |           |       |  
         Tiger        Lion        Cat     Dog   
      
Inheritance => is-a relationship **
Aggregation => has-a relationship  # Controller - Service - DAO layer

# aggregation vs composition vs association

Tiger is a Animal     - TRUE
Lion is a Animal      - TRUE
Cat is a Animal       - TRUE
Dog is a Animal       - TRUE
SEmployee is a Animal - FALSE 

        FileWriter
pdf excel ppt word  csv txt

LED TV is a TV
LCD TV is a TV
Laptop is a TV

SOLID Principles :  
--------------------
S - Single Responsibility Principle**
O - Open-Closed**
L - Liskov Substitution
I - Interface Seggregation
D - Dependency Inversion**
'''

class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):   # Inheritance    Tiger is-a Animal

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def sleeping(self):
        print("SUB  :: Tiger Sleeping")

# Write Lion, Cat, Dog classes and call methods


print("--------super class object creation--------")
anim = Animal()
anim.eating()
# anim.sleeping()  # ERROR

print("--------sub class object creation--------")
tiger = Tiger()   # Tiger tiger = new Tiger()  int x = 10
tiger.sleeping()  # sub class specific method
tiger.eating()    # inherited super class method
# tiger.roaring()  # ERROR
