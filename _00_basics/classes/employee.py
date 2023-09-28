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

