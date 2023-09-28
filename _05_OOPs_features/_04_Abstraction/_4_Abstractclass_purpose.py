'''

'''

'''
abstract method vs concrete method 
----------------------------------
only signature        sign. + body 

Problem with regular inheritance with class in Method Overriding scenario

                    Animal :
                      eating()  : abstract method 
                        
    Cat         Dog           Snake      Tiger        
    eating():      eating():    eating():    eating():
        ownbody      ownbody      ownbody        ownbody

# Normal Class
 For a method ( eating() ), the impl. is common for all sub classes

# Abstract class
Few methods need to be implemented in common way for all sub classes 
Other methods need to be implemented in unique way for all sub classes 

# Interface
For a method ( m1() ), the impl. is unique  for each sub class

'''


'''
  Super class       Sub class
  ================================
class A:              class B:
-----------------------------------
I. Super class is controlling sub class 
 Ex1:  m1()              0           ==> Sub class will inherit method from super class
 Ex2: m1() m2()         m1() m2()    ==> Sub class inherits super class 2 methods

==> As a sub class   (70% usage)
        I. Reuse super class methods 
        II. Override super class methods 
        --> But dont create your own methods 
        Here super class is controlling all sub classes 
        
        ==>. Employee emp = SoftEmp()** 
        

II. (30% usage)
    Super class is not controlling sub class(Sub class can define their own methods)
 Ex:  m1() m2()         m3() m4()        ==> Sub class inherits super class 2 methods + its own 2 methods
 Ex:  m1() m2()         m1()* m3()       ==> Sub class inherits super class 2 methods,its own 1 method
                                        overriden method m1()
                                        inherited method m2()
                                        own specific methods m3()
    SoftEmp semp = SoftEmp() 
   
   
   
   
    Why should I override ?
    Java: Specification/Protocol
    
        SuperClass:
        -------------
        As a super class I am providing the methods as per req.
            - As a sub class listen to me
                
                - Either reuse methods AS IS through Inheritance
                - Or override methods and provide your own body 
                        - BUT Dont create your own methods.
            
        
        
        
        
        
        
    
    
'''

