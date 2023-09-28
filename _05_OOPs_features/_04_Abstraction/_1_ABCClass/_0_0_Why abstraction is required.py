''''''
# Abstraction : Hiding the implementation details
# Class : AbstractClass : Interface
#   0%     0% to 100%       100%
# SOLID Principles

'''
     Employee 
          Address
       
UI -->   VehicleOperations
             Vehicle (has-a)
                  logic                Vehicle : 
                                         Car 
                                         Bike
                                         Cycle 
                                         Lorry 
                                         Van 
                                         Bus 
                                         Train
HighLevel Module : VehicleOps 
Medium           : Vehicle
LowLevel Modules : Car, Bike, Cycle, Lorrry, Van 
   
     Vehicle v = Car() 
                       
                         Vehicle 
                              get_fuel()
                              get_mileage()
                              get_info()
                              
               Car   Bike   Cycle Lorry Van Bus Train   Aeroplane
                c1()                                        
                get_fuel()
                get_mielage()
           
          Vehicle v = Car()   # float x = 10    5L can <--- 2L water
          v.get_fuel()       YES
          v.get_mileage()()  YES
          v.get_info()       YES 
          v.c1()             NO        
'''


"""
                              Animal

                 Cat    Dog              Tiger Lion     Monkey

Super class : Common/Generic behavior
Sub class   : Specific behavior wrt sub class


# SC 1 :When few methods are same for all sub classes,
        few are unique for each sub class #1
        
#1 .Below is the perfect example of using inheritance
                           Animal
                              eating()
                  Cat      Dog     Tiger      Lion
                    c1()    d1()     t1()       l1()

#2. Methods ==> Only in Super class : **This is WRONG apporach**
    Animal,Employee : Unnecessarily other behavior also will come to our sub class

                           Animal
                              eating() c1()    d1()     t1()       l1()
                  Cat      Dog     Tiger      Lion

#3. Methods ==> ****  This is wrong apporach ****
Only in Sub classes : Code duplication.
For example one method is common for all classes,then code duplication will happen

                  Cat        Dog         Tiger      Lion
                    c1()       d1()       t1()        l1()
                    eating()   eating()   eating()    eating()




# SC 2 :When all the methods are same for all sub classes
                           Animal
                                eating()
                                running()
                                sleeping()
                  Cat      Dog     Tiger      Lion

# SC 3 :When combination of common,different implementation required

                           Animal
                                eating()    #body
                                running()   #body
                                sleeping()  #dont give body  (required in unique way)

                  Cat          Dog       Tiger      Lion
                  sleeping() sleeping() sleeping() sleeping()   # Method overriding

So solution here is : make sleeping() method as "abstract method" not concrete method


SC: Each sub class wants their own body uniquely.

                           Animal
                                eating()    # Why should i provide body here ?
                                   
                  Cat          Dog       Tiger      Lion
                    eating()    eating()  eating()    eating()

"""
class Animal:
     def __init__(self):
          pass
     def eating(self):  # eating() is required for all sub classes,but they required in unique way
          print("Animal eating")

class Cat(Animal):
     def __init__(self):
          pass
     def eating(self):
          print("Cat Eating")

class Tiger(Animal):
     def __init__(self):
          pass
     def eating(self): #method overidiing
          print("Tiger Eating")

animal = Animal()
animal.eating()
cat = Cat()
cat.eating()
tig = Tiger()
tig.eating()
print("-----------------------")