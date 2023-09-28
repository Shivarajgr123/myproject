''''''
'''

def eating(self):
    print("SUPER :: Animal : eating")
    ....
Method:
         I. Method Signature   ==> def eating(self):
        II. Method Body(impl.) ==> print("SUPER :: Animal : eating") ...

Signature + Body : Function / Method** / Concrete Method

Code reusability :  1. Signature + Body (Implementation) (USe AS IS)
                    2. Only Signature                    (Override method)

'''

'''  
REUSE*
I: All sub classes requires - complete Method AS IS 
                                common - method signature  
                                common - method body(implementation)
                
                        Animal
                          - eating()
                          
                 Tiger   Lion     Cat   Dog
'''
class Animal:

    def __init__(self):
        pass
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):

    def __init__(self):
        pass
        print("SUB  :: Tiger constructor")

class Lion(Animal):

    def __init__(self):
        pass
        print("SUB  :: Lion constructor")

class Cat(Animal):

    def __init__(self):
        pass
        print("SUB  :: Cat constructor")

class Dog(Animal):

    def __init__(self):
        pass
        print("SUB  :: Dog constructor")

ani = Animal()
ani.eating()
print("----------")
tiger = Tiger()
tiger.eating()
print("----------")
lion = Lion()
lion.eating()
print("----------")
cat = Cat()
cat.eating()
print("----------")
dog = Dog()
dog.eating()
print("----------")