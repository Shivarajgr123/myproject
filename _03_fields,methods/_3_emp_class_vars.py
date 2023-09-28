
print("----Without class variables---------")
class Employee:
    # instance variables - each object has their own data
    # Here problem is "company name" is sharable to all employees(objects)
    def __init__(self, eid, name, sal, company):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.company = company  # It should be class variable

    def get_edata(self):
        print("Employee information :", self.eid, self.name, self.sal, self.company)

madhu = Employee(100, 'Madhu N', 15000, 'ORACLE SERVICES')
madhu.get_edata()
dilip = Employee(101, 'Dilip B', 25000, 'ORACLE SERVICES')
dilip.get_edata()

print("----With class variables---------")
x = 10
print("Value of x: ", x)

class Employee:
    comp = 'ORACLE SERVICES'  # class variable, this is sharable to all objects
    print("------Company Name-----------: ", comp)

    def __init__(self, eid, name, sal):  # local variables
        self.eid = eid   # LHS instance variables
        self.name = name
        self.sal = sal

    def get_edata(self):  # instance method
        # print(comp)
        print("Employee information :", self.eid, self.name, self.sal, Employee.comp)  # This is correct
        print("Employee information :", self.eid, self.name, self.sal, self.comp)  # XXX

print("Company Name : ", Employee.comp)  # Before creating object

madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()  # obj.methodname()  ==> Employee.get_edata(madhu)

akhil = Employee(101, 'Akhil Kumar', 15000)
akhil.get_edata()  # Employee.get_edata(akhil)

'''
When to use Instance method
    - When I have to write business logic wrt instance variables
    -    "                      "         wrt instance+class variables 

When to use Class Method 
    - When I have to write business logic wrt class variables

'''
