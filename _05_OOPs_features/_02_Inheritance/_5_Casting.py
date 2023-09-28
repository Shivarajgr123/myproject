

'''
'''
'''
Water = Data
Can   = Memory

    Watercan            Water              
    =====================================================
    1. 2L Can      <--- 2L of water         -  OK                          int x = 10
    2. 5L Can      <--- 5L of water         -  OK                          float x = 10.5
    3. 5L Can      <--- 2L of water         -  OK        Memory Wastage    float x = 10    ==> 10.0
    4. 2L Can      <--- 5L of water         -  NOT OK    Data Loss         int x = 10.5  ==> 10
                                                                           int x = (int)10.5 ==> 10
    class Employee:    # 5L can
    
    class SoftEmp(Employee):   # 2L can
     
        
        can    water
        --------------
     1. int x = 10       # 2L can <--- 2L water
     2. float x = 10.5   # 5L can <--- 5L water
     3. float x = 10     # 5L can <--- 2L water    # Implicit casting  ==> 10.0
 XX  4. int x = 10.5     # 2L can <--- 5L water    # Explicit casting  ==> 10    
                                                      int x = (int)10.5
    
    

    Employee
      |  m1()
      |
    SoftEmp
         m2()
         m1()

I.  Employee emp = Employee()   float x = 10.5
II. SoftEmp  emp = SoftEmp()    int  x  = 10
III.Employee emp = SoftEmp()**  float x = 10   5L can <------ 2L water  # Upcasting
IV. SoftEmp emp = Employee()        int x = 10.5   2L can <------ 5L water  # Downcasting
                                int x = (int)10.5
emp.m1()
emp.m2()  # ERROR

As a sub class you can reuse super class methods  AS IS 
  OR
Override super class methods
 BUT 
Dont create your own methods in sub class






    
                    Capacity          Content
    --------------------------------------------
int x   = 10        1. SoftEmp emp  = SoftEmp(100, 'MadhuN', 15000)     2L Can  <--- 2L Water  
float x = 10.5      2. Employee emp = Employee(100, 'MadhuN', 15000)    5L Can  <--- 5L Water
float x = 10        3. Employee emp = SoftEmp(100, 'MadhuN', 15000)***  5L Can  <--- 2L Water   Memory loss # Upcasting
int x = 10.5        4. SoftEmp emp  = Employee(100, 'MadhuN', 15000)    2L Can  <--- 5L Water   Data loss   # Downcasting

'''

'''
    Why should I override ?
    Java: Specification/Protocol
    
        SuperClass:
        -------------
        As a super class I am providing the methods as per req.
            - As a sub class listen to me
                - Either reuse methods AS IS through Inheritance
                - Or override methods and provide your own body 
                        - BUT Dont create your own methods.
            

IEEE standards 

    Employee
      |  m1()
      |
    SoftEmp
         m2()
         
I. SoftEmp semp  = SoftEmp(100, 'MadhuN', 15000)
semp.m1()
semp.m2()

II. Employee emp  = Employee(100, 'MadhuN', 15000)
emp.m1()

SUPER CLASS:
============
As a sub class, use my super class methods AS IS   (or) 
                                           Override my super class method
                        but don't write your own methods
                         

    Employee
      |  m1()
      |
    SoftEmp
         m2()
         
         
III. Employee emp = SoftEmp(100, 'MadhuN', 15000)  *******************
emp.m1()
emp.m2()  # ERROR



    Employee
      |  m1()
      |
    SoftEmp
         m1()
         m2()
         
Employee emp = SoftEmp(100, 'MadhuN', 15000) 
emp.m1()
emp.m2()  # ERROR
        

    Employee
      |  m1()
      |
    SoftEmp
         m2()
         m1()
Employee emp = SoftEmp(100, 'MadhuN', 15000) 
emp.m1()
emp.m2()  # ERROR

   
   
   
   Employee emp = SoftEmp(100, 'MadhuN', 15000)
   
   - If we create our own methods in subclass : USELESS 
   - It means that, either use super class method 
                     AS IS or  Override it 
                but dont create your own methods in sub class 
                
   
         
'''