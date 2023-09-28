from abc import ABC, abstractmethod
'''
Access modifiers:  private public default protected
_ __




4. ABSTRACTION :
===================
Hiding the implementation details i.e, method body wrt Inhertiance
Super class can be : 
        Class         : When sub classes need reusable components
                      : 0% abstraction
        Abstract Class: When sub class requires only signature
                            1. With all concrete methods : 0% abstraction
                            2. With all abstract methods : 100% abstraction
                            3. Both abstract,concrete
                                    1 concrete, 2 abstract methods: 66.6666%  
                                    2 cocrete, 2 abstract methods : 50%  
                             
        Interface     : All abstract methods : 100% abstraction 


Inheritance: Super class Sub class
           : When all sub classes has common features ==> Define Methods Super class with body
		   : When all sub classes has unique implementation ==> 
		               - Make class as Abstract class(super class)
		               - Define abstract methods* in super class
Abstraction : 0 to 100%
0%   -- In super abstract class,all are concrete methods      define - Class
30%  -- 10 methods - 3 abstract methods + 7 concrete methods  define - Abstract Class
100% -- In super abstract class, all are abstract methods     define - Interface

Employee emp = new SoftwareEmployee()
Polygon poly = new Triangle()
poly.noofsides()
poly.get_data()

    Select Polygon: Triangle 
                    Quadrilateral
                    Pentagon 
                Submit

class GetShape: 
    private Polygon poly;  # has a 
    def GetShape(this, poly):
        this.poly = poly
        
# DIP: Dependency Injection    
Polygon poly = Quadrilateral()
GetShape gs = GetShape()

Employee:           # has-a
    Address
    
            Address
    CurrAdd PermAddr ParentsAddr
    
Address ca = CurrentAddress()
Employee emp = Employee(100,"MadhuN",1000, ca)

    
GetShape:           # has-a
    Polygon  
      


DownloadFile:
    Writer 
    
               Writer 
        PdfW  ExcelW   WordD
            
    Select Writer: PdfWriter 
                   ExcelWriter
                   WordWriter
                   
                Submit


class Writer:
    def __init__(self):
        pass
    def write(self):
        pass
    def read(self):
        pass

class PdfWriter(Writer):
    def execute(self):
        pass


Writer w = PdfWriter()
Writer w = ExcelWriter()
Writer w = WordWriter()

w.read()
w.write()
# w.execute()

High level modules : Employee, DrawShape, DownloadFile, PlaceOrder
---------------------------------------------------------
Medium: Abstraction: Address, Polygon, Writer, CustomerAddress
---------------------------------------------------------
Low level modules  :    CurAddress,PermAddress,ParAddress 
                       Triangle, Quadrilateral, Pentagaon ....
                       PdfWriter, ExcelWriter, WordWriter 
                       HomeAddresss, OfficeAddress

Abstraction      Low Level 
---------------------------------
Employee emp = SoftwareEmployee()                       

Onboarding: 
    Employee 
    
emp.createrecord()


'''
class Polygon(ABC):  # Polygon is Abstract Class (Abstract Base Class)

    @abstractmethod
    def noofsides(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Triangle with 3 sides")

    # overriding abstract method
    def get_data(self):
        print("TRIANGLE  data")



class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")

    # overriding abstract method
    def get_data(self):
        print("Quadrilateral data")

# Here define Polygon as Interfeace instead of Abstrct class


'''
Polygon --> m1() m2()
Triangle --> m1() m2() m3()

Triangle t1 = new Triangle()  # 2L can <--- 2L water
    ==> We can create our own methods in sub class

t1.m1()
t1.m2()
t1.m3()


Polygon --> m1() m2()
Triangle --> m1() m2() m3()

Polygon p1 = new Triangle()   # 5L can <---- 2L water
    - Create object for sub class, and give reference to super class
    - creating our own methods in sub class ---> NO USE

p1.m1()  
p1.m2()
p1.m3()  # ERROR


'''

class DeliveryAddress(ABC):
    def __init__(self):
        print("DA Init")

    @abstractmethod
    def get_address(self):
        pass

class HomeAddress(DeliveryAddress):
    def get_address(self):
        print("Home Address")
class OfficeAddress(DeliveryAddress):
    def get_address(self):
        print("Office Address")

class PlaceOrder:
    def __init__(self, orderid:int, addr: DeliveryAddress):
        self.orderid = orderid
        self.addr = addr

    def confirm_order(self):
       print("Placing Order :", self.orderid, self.addr, self.addr.get_address())

# Customer has selected HomeAddress and placed the order

addr = HomeAddress()
po = PlaceOrder(1001, addr)
po.confirm_order()


'''
High level module:  PlaceOrder
Abstraction:  DeliveryAddress
Low level module : HomeAddress, OfficeAddress

DIP(Dependency Inversion Principle): 
- High level, Low level modules should not direclty depend on each other
- Both should have abstraction(medium)

IOC Design Pattern: 
--------------------
    - At runtime based on user selection from UI 
        dependency will be injected automtically 
        DeliveryAddress da = OfficeAddress()
        Animal a = Tiger()
        Animal a = Monkey()
        

Open Closed Principle:
------------------------
- Open for Extension: add one more animal Monkey 
- Closed for Modification: dont disturb  Highlevel or Medium 

'''
