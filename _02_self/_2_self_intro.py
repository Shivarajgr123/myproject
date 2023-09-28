10
x = 10
print("1. DataType/DataStructure    : Integer : Printing content : ", x)

def get():
    print("Function get()")


# get()  # Function call

print("2. Function : Printing Address :", get)  # Function name    x = 10   get = <func addr>


# print("Employee address : ",Employee)

'''
Here python will load the class Employee and provides memory for class body'''
x = 10
# Employee = <body of Employee>

class Employee:
    # STATE
    def __init__(self, eid, name, sal):
        # print("Self address  ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
    # BEHAVIOR
    def get_e_info(self):
        print("Employee details are : ", self.eid, self.name, self.sal)

    def apply_hike(self, score):
        print("Before hike : ", self.eid, self.name, self.sal)
        if score > 5 or score < 0:
            print("Invalid Data")
        else:
            esal = self.sal
            if score == 5:
                esal += esal*30/100
            elif score == 3 or score == 4:
                esal += esal*20/100
            elif score == 2:
                esal += esal * 10 / 100
            elif score == 1:
                print("No salary hike")
            else:
                print("Sorry. You got terminated")
                return
            self.sal = esal
            print("After hike : ", self.eid, self.name, self.sal)


print("3. Class: Prints Path of class : ", Employee)

madhu = Employee(100, 'Madhu Nettem', 15000)  # object/instance/ref. variable
print("4. Object : Employee object  : ", madhu)

madhu.get_e_info()
print("Madhu salary : ", madhu.sal)
print("---------------------------------------------------")
print("Employee address : ", Employee)
print("-----------------------------------------------------")
'''
Object creation:
---------------------
init method: Helps to construct object by initializing the data 
 
Step1 : Object creation : 2 parts : 
             I. Employee  
            II. (100, 'Madhu Nettem', 15000)
Step2 : Python will check and find the address of Employee
Step3 : First python creates empty object(wrapper) of Employee class
        Employee class __init__ method will be called, 
        passes 
                1. Address of empty object to self parameter         ==> self
                2. the tuple of arguments will be passed to remaining parameters  ==> (eid, name, sal) 
Step4 : Data passes to local variables (eid, name, sal)               
Step5 :         self.eid = 100 
                self.name = 'Madhu Nettem'
                self.sal = '15000'
                            LHS eid = instance variable
                            RHS eid = local variable 
        ==> Local variable eid data,we are setting to instance variable 

Step 6: Once object construction is done, address will be given to madhu        

Note:
--------
-  Inside object data will be initialized.
- __init__ method helps to initialize the STATE of object(instance)


'''

print("Madhu object : ", madhu)
madhu.get_e_info()


madhu = Employee(100, 'Madhu Nettem', 15000)
jai = Employee(101, 'Jaykar', 20000)
ajay = Employee(102, 'Ajay S', 25000)

emps = [madhu, jai, ajay]
rating = {100: 5, 101: 4, 102: 3}

print("----Salary hike of each employee------")
for emp in emps:
    sal = emp.sal
    rate = rating[emp.eid]
    emp.apply_hike(rate)














