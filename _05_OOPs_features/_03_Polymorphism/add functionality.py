x = 10
print(x)  # x.__str__()
print(x.__str__())

li = [1, 2, 3]
print(li)
print(li.__str__())

class Employee(object):

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

madhu = Employee(100,'Madhu Nettem',140000)
print("Employee object : ", madhu)  # madhu.__str__()

# Override it

class Employee(object):

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_data(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    def __str__(self):  # Overriden method from object class
        return ''.join([str(self.eid), "*", self.name, "*", str(self.sal)])

madhu = Employee(100,'MadhuNettem',15000)
print("Madhu object : ", madhu)   # madhu.__str__()
print("Madhu object : ", madhu.__str__())
