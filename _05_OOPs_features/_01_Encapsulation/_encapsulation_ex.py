'''
Capsule:
 _______

(::::: )

'''
'''
Encapsulation :  Binding the "data members" and 
                             "member methods" 
                                      into single entity
                                      
                                        - data members   ==> Fields
                                        - member methods ==> Methods
                                        - Entity         ==> Class
                Ex: Class, object
                
                           |  Logical   |  Physical 
                           -----------------------
                    Class  |  Fields    |  Methods
                    ------------------------------
                    Object |  Methods   |  Fields

1. Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes  (class,instance variables)
member methods : Methods (Instance / Class / Static Methods)

madhu = Employee(100,'Madhu N, 15000)

Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


madhu = Employee1(100,"MadhuN",15000)


'''

'''

'''
# Binding data members and member methods into single entity
'''
Encapsulation :  Binding the data members and 
                             member methods into single entity
                                        - data members   ==> Fields
                                        - member methods ==> Methods
                Ex: Class, object
                
                              Logical     Physical 
                    --------------------------------
                    Class  |  Fields      Methods
                    object |  Methods     Fields
                
                '''
# capsule

class Employee:
    # STATE --> data members  *  logical
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical
    def get_details(self):
        print("Employee details")

# Employee.get_details()
obj = Employee(1001, 'MadhuN', 10000)   # data physical methods logical
obj.get_details()
'''
Class   - Variables - Logical    <===>  Methods  - Physical
Object  - Variables - Physical    <===>  Methods  - Logical
'''