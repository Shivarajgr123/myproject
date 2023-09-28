''''''
'''
              Person
            Father  Mother 
                Child 
            
                Person
                    display()
            Father     Mother
               display()   display()
                     
                  Child  
                
                
                '''
class Person:
    def display(self):
        print("Person called")


class Father(Person):
    pass
    '''
    def display(self):
        print("Father called")
    '''

class Mother(Person):
    pass
    '''
    def display(self):
        print("Mother called")
    '''

class Child(Father, Mother):
    pass


child_obj = Child()
child_obj.display()

for ca in Child.__mro__:
    print(ca)