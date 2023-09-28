
'''
https://www.geeksforgeeks.org/operator-overloading-in-python/
'''
# Everything is an object in Python ***
'''
Operator Overloading: Behavior is same but operands may change
'''
# Operator overloading
# 10 + 20  10+20+30   1+2   1+2+3   "Hello" + "World"  [1,2,3] + [4,5,6]

x = 10  # int(x)
y = 20
print("Addition : ", x + y)  # x.__add__(y)  1+2
# x is an object of type int class.Created object for int class
# x.__add__
x.__add__(y)
10 + 20
10 + 20 + 30 + 40  # 10.__add__(20,30,40)

list1 = list()
x = 10.5
y = 20.2
print("Addition : ", x + y)  # x.__add__(y)

str1 = 'Hello'
str2 = 'World'
print("Addition  :", str1 + str2)  # str1.__add__(str2)

dict1 = {1:1}
dict2 = {2:3}
print(dict1+dict2)


# create 2 employee objects and add their salaries
class Employee(object):
    pass