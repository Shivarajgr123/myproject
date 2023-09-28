class Employee:

    def __init__(self, eid, name='Madhu N', sal=1000):  # Constructor Overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading
madhu = Employee(100)
madhu = Employee(101, 'Yugandhar')
kiran = Employee(102, 'Kiran Kumar', 20000)


'''
class Employee:
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)
        
emp = Employee(100,'Madhu',20000)
       
'''