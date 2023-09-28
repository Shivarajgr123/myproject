'''
Object Oriented Programming System
Everything is an object in Python***
'''

'''
Class/Object
------------------
Encapsulation
Abstraction
Inheritance
Polymorphism
'''


'''
Entity            : Class   : Employee 
---------------------------------------
State    : Attributes/Fields : eid, name, sal, mobile, address, emailid
Behavior : Methods           : CRUD : Create, Retrieve, Update, Delete  
                               4*3 - 12 Functions
                              Create  : one emp / multiple / all 
                              Retrieve: one emp / multiple / all
                              Update  : one emp / multiple / all
                              Delete  : one emp / multiple / all
'''

# REQUIREMENT : Find sum of  given two numbers

# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))

# BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result

print("Sum: ", get_sum(n1, n2))
output = get_sum(n1, n2)
print("Sum: ", output)


# str = 'hello' # str("hello")
# str.split()
'''
Employee  / GMAIL ACCOUNT (SIGNUP/LOGIN/UPDATE/DELETE ACC)
CRUD operations:
-----------------
    - CREATE EMPLOYEE
    - RETRIEVE EMP DETAILS SINGLE/PARTIAL/ALL
    - UPDATE EMP DETAILS   SINGLE/PARTIAL/ALL
    - DELETE EMP DETAILS   SINGLE/PARTIAL/ALL
    
'''

# print("Sum of 2 numbers is : ", get_sum(n1, n2))


'''
Blocks in Python: 
   if elif else 
   for while 
   functions 
   class 
   try except else finally 
   with
'''

'''
Why OOPs
 - Security - STATE
 - Grouping - BEHAVIOR 
'''

# A1 :: Using Functions
print("---------Using Functions-----------")
'''
Disadvantages:
    1. Security for data
    2. Grouping of behavior
'''
    # 1. STATE
empid = 100  # int(input("Enter empid :"))
name = 'Madhu Nettem'  # input("Enter name : ")
sal = 15000  # float(input("Enter sal :"))

    # 2. BEHAVIOR
def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)

get_einfo(empid, name, sal)

'''
# class syntax 

class <ClassName>: # class Employee:
    # STATE 
    # BEHAVIOR

class Addition:
        #1. STATE
    n1 = 10          # a. static way: No USE
    n2 = 20
        #2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result
        
b. Dynamic way: n1 = int(input("Enter number1 ")): No USE
                n2 = ......
                        Not a better idea 
             
c. Solution: Create Constructor **
-----------------------------------
    def __init__(self, n1, n2):   # init method / constructor 
        self.n1 = n1 
        self.n2 = n2
         
             
'''

# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
class <ClassName>:
     # STATE  (Data type/structures)
     # BEHAVIOR (CRUD) 

'''

'''
Java: 
        int x = 10;  Direct initialization 
        
        int x;  # Declaration
        x = 10  # Initialization

Python :  x = 10

'''

# Using OOPs  -- Class
# Step 1:
class Employee:
    # 1. STATE
    empid = 100  # int(input("Enter empid :"))
    name = 'Madhu Nettem'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)

print("------------------Using OOPs-------------------------")

# Create a class

class Employee:
    # State
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # Behavior
    def get_einfo(self):
        print("Employee info : ", self.eid, self.name, self.sal)

# Object creation
madhu = Employee(100, 'Madhu N', 10000)
# Method Call
madhu.get_einfo()

print("==================================================")
vikram = Employee(100, 'Vikram Magala', 15000)
'''
At runtime, Object creation
            # 1. Divides RHS into 2 parts 
                      I. Employee  
#                    II. (100, 'Vikram Magala', 15000)
              2. Creates wrapper withe empty memory slot
              3. Goes to Employee class and calls init method
              4. Passes wrapper address to self, rem. tuple of args to other parameters
              5. Inside wrapper data will be initialized 
              6. Once object creation is done, it will be given a name(LHS) i.e, vikram
'''
# 3. Method call
vikram.get_einfo()
'''
    At runtime, During method call 
          1. Python will find type of object vikram : class Employee 
          2. It will verify for the method get_einfo() inside class Employee 
          3. If exists, 
               - method call happens, by passing vikram object to self 
               - Completes method execution
                
           

'''


# Step1: Create Class
class Student:
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # Behavior
    def get_sinfo(self):
        print("Student Information: ", self.sid, self.name, self.marks)

    def update_marks(self, val):
        self.marks = val

    def del_marks(self):
        self.marks = None

# Step2: Create Object
bhargav = Student(100, "Bhargav Sai M ", 65)
# Step3: Method Call
bhargav.get_sinfo()
bhargav.update_marks(90)
bhargav.get_sinfo()
bhargav.del_marks()
bhargav.get_sinfo()








msg = str('Hello World')
res=msg.capitalize()
print((res))


# Student class

class Student:
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # Behavior
    def get_sinfo(self):
        print("Student info : ", self.sid, self.name, self.marks)

    def get_result(self):
        if self.marks >= 35:
            print("Result : PASS : ", self.name)
        else:
            print("Result :FAIL  : ", self.name)

    def update_name(self):
        self.name = "Vigneshwaran Kanagaraj"



vignesh = Student(100, 'Vignesh K', 56)
print("Beore update : ", vignesh.get_sinfo())
vignesh.update_name()
print("After update : ", vignesh.get_sinfo())



li = [1, 2, 3]
li.reverse()

str1 = 'Hello World'
str1.capitalize()



print("-------------------------------------------------------------")

ajay = Employee(101, 'Ajay S', 20000)
ajay.get_einfo()
'''
During method call:
1. Python will find type of object i.e, madhu is of type Employee class
2. It will go to the class(Employee) and will check whether method exists or not.
3. During method call: passes object madhu to self

'''
print("Madhu object: ", ajay)



x = 10
print("Value : ", x)
x = int(10)
li = list([1, 2, 3])
li.append(10)
st = str('Hello')
# st.append(100)

class Student:
    # STATE
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # BEHAVIOR
    def get_sdata(self):
        print("Student Information: ", self.sid, self.name, self.marks)


class Pen:
    # STATE
    def __int__(self, pid, name, price, color):
        self.pid = pid
        self.name = name
        self.price = price
        self.color = color

    # BEHAVIOR
    def get_peninfo(self):
        print("Pen Details : ", self.pid, self.name, self.price, self.color)



x = 10     # int(10)
x = int(10)

msg = 'Hello World'  # str('Hello World') ==> str.__init__('Hello World')
msg = str("Hello World")
msg.capitalize()  # 40 functions/Methods







print("--------------Student example in OOPs--------------")

class Student:
    # 1. STATE
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    # BEHAVIOR
    def get_sinfo(self):
        print("Student Details : ", self.sid, self.name, self.marks)

madhu = Student(100,'MadhuN', 65)
madhu.get_sinfo()



# CREATE 100 classes

'''
TV 
Pencil
Pen 
Mobile  
Laptop 
Book  
Charger 
Dog 
Fan 
Light


'''









print("--------------TELEVISION example in OOPs--------------")

class Television:
    # STATE
    def __init__(self, tid, brand, price, color):
        self.tid = tid
        self.brand = brand
        self.price = price
        self.color = color

    # BEHAVIOR
    def get_telinfo(self):
        print("Television info : ", self.brand, self.price, self.color)

samsung = Television('L0001', 'Samsung', 25400, 'Black')
samsung.get_telinfo()


# 50 different class examples

