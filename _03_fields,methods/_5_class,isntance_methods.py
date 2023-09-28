
'''
class structure
    # 1. Fields  - STATE
         class variables    - at class level,when state is shared among objects
         instance variables - at instance level, inside init method.
                              When each object required separate data

    # 2. Methods - BEHAVIOR
   C  I
   -----
   T  F     class method       - cls parameter,which works only on class variables
   F  T     instance method    - self parameter,which works on only instance variables
   T  T                                                         both instance,class variables
                                                            only class variables XXX
   F  F     static method       - generic method

'''
class Employee:
    def __init__(self):
         pass

    @staticmethod
    def get_edata():
        print("Employees info : generic behavior")

# no need to create object to call class methods
Employee.get_edata()  # Employee.get_edata()

#2 way - Don't do it
obj = Employee()
print("Object address : ", obj)
obj.get_edata()  # ==> Employee.get_edata(obj)

print("------All methods---------")
class Employee:
    e_count = 0        #  Sharing + Modify
    office = 'ORACLE'  # Sharable

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)

    def get_empinfo(self):
        print("Employee details : ", self.eid, self.name, self.sal)
        print("Class data : ", Employee.e_count, Employee.office)
        print(Employee.get_edata())
        print(self.get_edata())   # XXX

    @staticmethod
    def get_static():
        print("Employees info : generic behavior")


Employee.get_edata()   # class method
Employee.get_static()  # static method
# to call instance method
madhu = Employee(101, 'Madhu Nettem', 15000)
madhu.get_empinfo()
madhu.get_edata()
Employee.get_edata()


print("-----static method--------")

# i want a behavior which neither deals with class variables nor instance variables

class Employee:
    @staticmethod
    def getinfo():
        print("Static method implementation")
    @classmethod
    def get_class(cls):
        print("Class method Implementation")


Employee.getinfo()   # preferrable way
Employee.get_class()

emp = Employee()
emp.getinfo()   # dont use
emp.get_class()  # dont use

'''
Questions:
---------------
1. Class variables/ Instance Variables. Initialization ?
  - Class variables will be initialized first during loading of class(Only one time)
  - Instance variables during object creation
 
2. Can I use Class/instance variables inside instance method ?
  - YES.
    Because class variables were initialized first, we dont need object creation

3. Can I use instance variables inside class or static method ?
  -  NO  

4. My behavior is to work with only Instance Variables ?
  - Define Instance Method

5. My behavior is to work with Instance/Class Variables ?
  - Define Instance Method

6. My behavior is to work with only Class Variables ?
  - Define Class Method

7. I dont want either Class or Instance variables ?
  - Define Static Method

8. Using object/instance can I access all 3 Methods(class,static,instance) ?
  - YES

9. Can i access instance method using class ?
    NO 
    but if we have object ready 
        Employee.getdata(madhu)

10.Can I access class variables inside static method ?
    YES 
        -But dont try to access. 
        
11. Along with self, cls can we pass any other parameters ?
    YES 
12. Can I write other names for self,cls ?
       
'''


'''
class Employee:
    1. STATE
    ----------
    # class variables
    # instance variables ==> init method
    
    2. BEHAVIOR
    -------------
    # class method      : works only on class variables 
    # instance method   : works only on instance variables (OR)
                          works on both instance/class variables 
    # static method     : neither on class nor on instance variables 
'''
'''
class var                  instance var
-------------------------- ----------------------------
while loading class        at the time of object creation

class var                  instance var
class methods              instance methods

instance variables cant be used inside class method **

++ Within instance methods we can use class variables *****
viceversa is not True ==> within class methods we can't use instance varibales
'''


# UI --->   Python ---> Database

# Currently working as Software Engineer in Oracle from  Jun 2020 to till date
'''
Current employer: Oracle 
Designation : Software Engineer
From Date: June - 2020
To Date  : June - 2022

100 employees:
---------------
excel sheet
csv 

txt file 
---------
100,Madhu Nettem,15000,Bangalore,Oracle
101,
102,
....

Client                    Server      Drive

UI(Youtube)       --->    Python     ---->  Database

 
{'filenmae':
 'size':
 'ext':
 'format':
 'content':
 'drivepath':
}                         
                          
                          
                          
pdf file 
'''




