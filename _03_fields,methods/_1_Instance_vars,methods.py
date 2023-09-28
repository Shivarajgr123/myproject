''''''
'''
object / instance / ref. variable

CLASS ::    
           STATE     -  Fields
                            - Instance Variables*
                            - Class Variables
           BEHAVIOR  -  Methods
                            - Instance Methods*
                            - Class Methods
                            - Static Methods
'''

# x = 100
class Employee:
    # Fields  - STATE
    # Methods - BEHAVIOR
    pass

# object / instance / ref. variable
a = 100

class Employee:

    def __init__(self, eid, name, sal):  # parameters
                # RHS  - eid, name, sal ==> Local variables
                # self.eid self.name self.sal ==> Instance variables
        print("Self address : ", self)
        x = 10          # x is local variable
        self.eid = eid   # RHS eid is local variables
        self.name = name  # self.eid,name,sal : Instance Variables
        self.sal = sal


    # Instance Method
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)
        # print("value of x : ", x)

# Employee.get_edata()  # ERROR
print("---Employee-------", Employee)
madhu = Employee(100, 'MadhuN', 15000)

madhu.get_edata()          # Standard method call
# OR
Employee.get_edata(madhu)  # realtime projects we won't use this way of calling

'''
1. Python finds type of object i.e., madhu --> Employee
2. Goes to Employee class and verifies whether get_edata method exists or not 
3. If exits, then performs method call by passing madhu object to self of method
'''
# Alternate approach to call method
Employee.get_edata(madhu)



# madhu.get_edata()  # Employee.get_edata(madhu)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)
