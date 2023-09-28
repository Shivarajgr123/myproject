''''''
'''
class Class:
    # STATE  ==>  FIELDS
        1. Class variables
        2. Instance variables

    # BEHAVIOR ==> METHODS
       1. Class Method   : Work only with class vars
       2. Instance Method: Work with only instance vars/ both instance,class vars
       3. Static Method  : Neither instance nor class vars

Inside 
 Instance Method : Instance / Instance and Class vars  (Object creation mandatory)
 Class Method    : Class vars  (Obj. creation not required)
 Static Method   : xxx         (Obj. creation not required)

'''

# Get employee count at a given point of time.


class Employee:
    comp = 'ORACLE'  # Share
    emp_count = 0    # Share + Modify

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)
        print("Generic info : ", Employee.comp, Employee.emp_count)

    # class method (can access only class variables)
    @classmethod   # Decorator
    def get_ecount(cls):
        print("Employee count : ", cls.comp, " -- ", cls.emp_count)
        # print("Employee count : ", Employee.comp, " -- ", Employee.emp_count)

# To call class variables / class method, object is not required

print("Employee comp: ", Employee.comp)
print("Employee count: ", Employee.emp_count)
Employee.get_ecount()

madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()      # instance method ==> Employee.get_edata(madhu)
# To call class method
madhu.get_ecount()     # Yes, but don't use
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)

# To call class method, we can call using object,But don't do it.
# madhu.get_ecount()

jaya = Employee(101, 'Jayadeep  Chowdary A', 20000)
jaya.get_edata()
Employee.get_ecount()

mohan = Employee(102, 'Mohan Kumar', 45000)
mohan.get_edata()
Employee.get_ecount()

'''
btech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)

        
employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY 
            
   

class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object 
instance methods   : 1. To act only on instance variables OR 
                     2. Both instance and class variables
                     
                   
Accessibility:
---------------------
CV   - ClassMethod,    InstanceMethod 
IV   - InstanceMethod
 
'''