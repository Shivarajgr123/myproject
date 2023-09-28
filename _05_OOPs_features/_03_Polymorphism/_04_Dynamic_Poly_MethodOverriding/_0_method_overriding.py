


class Employee(object):

    def __init__(self, eid):
        self.eid = eid

    def __add__(self, other):
        return self.eid + other.eid

madhu = Employee(10)
kiran = Employee(20)

print("Add employee objects : ", madhu + kiran)  # madhu.__add__(kiran)


'''
                           Animal
                  Cat    Dog   Tiger    Lion

Own Specific method
Inherited method
Overriden method

'''


class Animal:
    def __init__(self):
        print("In Animal object")

    # Generic behavior
    def eating(self):
        print("Animal Eating")


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    # method overriding
    def eating(self):
        print("Cat is Eating")

cat = Cat()
cat.sleeping()
cat.eating()


# SCENARIOS
print("--------------------------")
class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # Specific behavior
    def barking(self):
        print("DOG is barking")

dog = Dog()
dog.barking()
dog.eating()

print("----------------------")
class Lion(Animal):
    def __init__(self):
        print("In LION object")

lion = Lion()
lion.eating()
print(lion) # lion.__str__