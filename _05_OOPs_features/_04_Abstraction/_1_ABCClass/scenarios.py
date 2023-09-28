from abc import ABC, abstractmethod
class Animal(ABC):
    x = 10
    def __init__(self):
        print("In Animal object")

    @abstractmethod
    def eating(self):  # Generic behavior
        pass

    @staticmethod
    def getinfo1():
        print("Static static : get info method")

    @classmethod
    def getinfo2(cls):
        print("Static static : get info method", cls.x)

    def get_edata(self):
        print("Instance Method ")

Animal.getinfo1()
Animal.getinfo2()
# obj = Animal()
