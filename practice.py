"""
print("*"*75)
class student:
    '''This is the developed by durga for demo purpos'''
print(student.__doc__)
print("="*75)
"""


"""
print("*"*75)
class student:
    ''' This class developed by durga for demo purpose'''
help(student)
print("="*75)
"""




# print("-------------------------start--------------------------------------")
# class Employee:
#     def __init__(self,eid,name,sal):
#         self.eid=eid
#         self.name=name
#         self.sal=sal
#
#     def get_einfo(self):
#         print("Employee info:",self.eid, self.name, self.sal)
#
# shiva= Employee(1235, "Shivaraj", 1000)
# shiva.get_einfo()
#
# print("-------------------------end--------------------------------------")


#print("-------------------------start--------------------------------------")
"""
class student:
    def __init__(self,sid,name,marks):
        self.sid=sid
        self.name=name
        self.marks=marks

    def get_sinfo(self):
        print("Student Information:",self.sid,self.name,self.marks)

    def update_marks(self,val):
        self.marks=val

    def del_marks(self):
        self.marks=None

shiva=student(100,"Shivarajkumar",5000)
shiva.get_sinfo()
shiva.update_marks(1000)
shiva.get_sinfo()
shiva.del_marks()
shiva.get_sinfo()
"""
#print("-------------------------end--------------------------------------")

"""
msg="shivarajkumar"
res=msg.capitalize()
print(res)
"""
"""
class student:
    def __init__(self,sid,name,marks):
        self.sid=sid
        self.name=name
        self.marks=marks

    def get_sinfo(self):
        print("Student info:",self.name,self.name,self.marks)

    def get_result(self):
        if(self.marks>=35):
            print("Result: Pass:",self.name)
        else:
            print("Result:Fail:",self.name)
    def update_name(self):
        self.name="Rajkumar"

s=student(100,"Shivaraj",95)
print("befor update:",s.get_sinfo())
s.update_name()
print("After update:",s.get_sinfo())
s.get_result()
"""
#print("-------------------------end--------------------------------------")
"""
li=[1,2,3,4,5,]
li.reverse()
print(li)
"""
"""
class Television:
    def __init__(self,tid,brand,color,price):
        self.tid=tid
        self.brand=brand
        self.color=color
        self.price=price

    def get_tel_details(self):
        print("The Details of the Television:",self.tid,self.brand,self.color,self.price)

t=Television("12zer213412","sony","Black",100000)
t.get_tel_details()
"""

print("-----------------------------------------------start---------------------------------")

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Create a new bank account
account1 = BankAccount("12345", "John Doe")

# Deposit and withdraw money
account1.deposit(1000)
account1.withdraw(500)

# Display account information
account1.display_account_info()


print("-----------------------------------------------end-----------------------------------")

class Aircraft:
    def __init__(self, registration_number, manufacturer, model):
        self.registration_number = registration_number
        self.manufacturer = manufacturer
        self.model = model

    def fly(self):
        return f"{self.manufacturer} {self.model} is now taking off."

    def land(self):
        return f"{self.manufacturer} {self.model} is landing safely."


class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.runways = []

    def add_runway(self, runway):
        self.runways.append(runway)

    def list_runways(self):
        return [runway.name for runway in self.runways]


class Runway:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def is_suitable_for_aircraft(self, aircraft):
        return self.length >= aircraft.min_runway_length


# Example usage:
if __name__ == "__main__":
    # Create aircraft
    aircraft1 = Aircraft("N12345", "Boeing", "747")
    aircraft2 = Aircraft("G-ABCD", "Airbus", "A320")

    # Create airport
    airport1 = Airport("JFK Airport", "New York")
    airport2 = Airport("LAX Airport", "Los Angeles")

    # Create runways and associate with airports
    runway1 = Runway("Runway 1", 3000)
    runway2 = Runway("Runway 2", 4000)
    airport1.add_runway(runway1)
    airport2.add_runway(runway2)

    # Check if an aircraft can use a runway
    print(f"{aircraft1.manufacturer} {aircraft1.model} can use {runway1.name}: {runway1.is_suitable_for_aircraft(aircraft1)}")
    print(f"{aircraft2.manufacturer} {aircraft2.model} can use {runway2.name}: {runway2.is_suitable_for_aircraft(aircraft2)}")

    # Perform flight operations
    print(aircraft1.fly())
    print(aircraft2.land())

