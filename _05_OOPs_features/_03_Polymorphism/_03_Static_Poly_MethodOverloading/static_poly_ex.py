'''

 .java   ---manual compilation ---> .class     --> runtime
 .py     ---------------------------.pyc---------> runtime

python interpreted programming language


Polymorphism : Ability to exists in multiple forms
2 types : Static Polymorphism  OR compile time poly. - Ex => Method Overloading
          Dynamic Polymorphism OR run time  poly.    - Ex => Method Overriding
'''
# Static polymorphism

'''
Method overloading** in other languages:
---------------------------------------
Java Code:
==========
class Employee:
    def getdata(eid):
        pass
    def getdata(eid, name):
        pass
    def getdata(eid, name, sal):
        pass
   
madhu = Employee()
madhu.getdata()     # ERROR
----------------------------------------------
madhu.getdata(10)                 1st Method
madhu.getdata(10, 'Madhu')        2nd Method
madhu.getdata(10, 'Madhu', 1000)  3rd Method

'''
x = 10
print(x)
x = 20
print(x)
print("-----------------Scenarios----------------------")

def getdata(eid):
    print("Data is : ", eid)

# getdata()  # ERROR
# getdata(10, 20)  # ERROR
getdata(10)  # Works

print("--------------------")
def getdata(eid, name):
    print("Data is : ", eid, name)

getdata(10)           # ERROR  |  In java it works
getdata(10, 'Madhu')  # WORKS

def getdata(eid, name, sal):
    print("Data is : ", eid, name, sal)

getdata(10)           # ERROR
getdata(10, 'Madhu')  # ERROR
getdata(10, 'Madhu', 1000)

# Solution is use one single method with default arguments for parameters

'''
in Python:
----------
def getdata(eid = 0, name = None, sal = 0):  # Method Overloading
    pass

getdata()
getdata(10)
getdata(10,'Madhu')
getdata(10,'Madhu',1000)   
getdata(name='Madhu', sal=1000) 
getdata(name='Madhu')
getdata(sal=1000) 


    In Python, we cant achieve Method overloading directly.
    Because only latest method will be considered.
    Indirect way of achieving method overloading in Python
    using default arguments
'''
def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()                   # getdata(id=None,name=None,sal=None)
getdata(10)                 # getdata(id=10,name=None,sal=None)
getdata(10, 'Madhu')        # getdata(id=10,name='Madhu',sal=None)
getdata(10, 'Madhu', 1000)  # getdata(id=10,name='Madhu',sal=1000)

'''
This method will exhibit Static polymorphism'''


# *args  **kwargs : Will see in decorator concept

