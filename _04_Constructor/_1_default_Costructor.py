'''
Constructors:
    Default Constructor
    Parameterized Constructor
'''
class Employee:
    pass

'''
converts as below
                        class Employee:
                            def __init__(self):
                                pass
'''
print("Employee class @ ", Employee)
obj = Employee()


class Employee:
    # Default constructor
    def __init__(self):  # Default constructor
        pass  # to perform any generic action

    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)

madhu = Employee()
madhu.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)




# while defining class, default constructor is not mandatory.
# Python give automatically



