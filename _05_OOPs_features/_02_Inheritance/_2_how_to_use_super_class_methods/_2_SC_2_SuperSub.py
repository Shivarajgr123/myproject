'''
Laptop Pendrive Car Bike

Pendrive : IEEE standards Specification

market standards
USB port measurements

Color, Size, Styles outer layer change



'''
METHOD_OVERRIDING_ = ''' OVERRIDE *

II: All sub classes required  : a. Common  signature      but 
                                b. Unique implementation

                            --> method signature -  common behavior  
                            --> method body      -  unique** implementation 


   If we write classes without inheritance as below,
                 Tiger   		Lion        Cat        Dog
					 eating()    ate()    i_am_eating()   we_ate()

	We cant understand common behavior. So this will not work out.
   
   Behavior : Signature
   Implement/Implementation: Providing Body 
   
    ==> We have to use inheritance mechanism here 
    
								Animal
									def eating():
									    body

                Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()
                        ownbody     ownbody      ownbody   ownbody
                        
Above mechanism is called as Method Overriding ***

'''

# METHOD OVERRIDING

class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal Eating :: Generic Behavior")  # Generic impl.

class Tiger(Animal):

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def eating(self):  # Method overriding
        print("SUB :: Tiger eating in specific manner ")   # own body/implementation

    def sleeping(self):
        print("SUB :: Tiger Sleeping : Own Method")

anim = Animal()
anim.eating()
# anim.sleeping()

tiger = Tiger()
tiger.sleeping()
tiger.eating()

class Polygon:
    def __init__(self):
        print("SUPER : POLYGON OBJ")
    def get_sides(self):
        print("More than 2 sides")

class Triangle(Polygon):
    def __init__(self):
        print("SUB : TRIANGLE OBJ")
    def get_sides(self):
        print("Triangle : 3 sides ")

class Quadrilateral(Polygon):
    def __init__(self):
        print("SUB : QUADRILATERAL OBJ")
    def get_sides(self):
        print("Quadrilateral : 4 sides")
