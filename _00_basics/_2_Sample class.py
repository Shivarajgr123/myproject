# Step1: Defining Class
'''
Security for State
Grouping common behavior
'''
class Employee:
    # STATE  # PIPPERMENT vs CHOCOLATE  vs BISCUIT PACKET
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # BEHAVIOR
    def get_einfo(self):
        print("Employee information : ", self.empid, self.name, self.sal)
x = 10
#Step2:  object creation
madhu = Employee(100, 'Madhu Nettem', 15000)  # Initialization
'''
Object creation:
------------------
1. Python will load class Employee 
2. It will call init method and passes arguments (wrapper_addr, other args)
3. Inside init, data will be initialized using self variable 
4. self address will be given to object i.e., madhu
'''
madhu.get_einfo()
'''
1. First Python will find type of object 
    madhu --> class Employee (madhu is of type Employee class)
2. It will check whether method exists in class or not 
3. It will call method by passing madhu object to self parameter(madhu obj addr to self)
4. Method execution will happen
'''
