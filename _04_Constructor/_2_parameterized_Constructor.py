''''''
'''

# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional Arguments
            - Default Arguments
            - Keyword Arguments

'''


# *********     1. Positional Arguments    **********
class Employee:
    # Parameterized Constructor
    # def __init__(self, eid: int, name: str, sal: float):
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

madhu = Employee(100, 'Madhu N', 1234.54)


# *********     2. Default Arguments    **********
class Employee:
    # parameterized constructors
    def __init__(self, eid=0, name=None, sal=0):  # Constructor Overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


# Constructor Overloading

madhu = Employee()
madhu.getedata()

chandra = Employee(201)
chandra.getedata()

chandra = Employee(201, 'Chandra Sekhar')
chandra.getedata()

madhu = Employee(200, 'MadhuN', 10000)
madhu.getedata()


# 3. Keyword arguments
raj = Employee(name='Rajesh', sal=20000)
raj.getedata()


# Constructor Overloading:
'''
When we are able to create object in minimum 2 or more ways 
its called Constructor Overloading
'''