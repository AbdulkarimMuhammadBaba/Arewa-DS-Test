countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
'''map iterates over a list and return a list, it takes a function and iteratable as a parameter; a filter function calls a specified function which returns boolean for each item in the iteratable while reduce function which is usually imported from the functools module, iterate over a list and return a single item,it also takes a function and iteratable as parameter
'''
#2
'''higher order functions are versatile python functions us toallowsyperations on other functions like using other functions as parameters, return them or even assigning them as variables; closure is a way of defining a function that can access another function nested within a python function while a decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
'''
#3
from functools import reduce
def square(num):
    return num ** 2


def vowel_initials(name):
    if name[0] in 'aeiouAEIOU':
        return True
    return False


def sum_of_squares(num1, num2):
    return num1 + num2

print(list(filter(vowel_initials, names)))
print(list(map(square, numbers)))
print(reduce(sum_of_squares, list(map(square, numbers))))
#4
for i in countries:
    print(i)
#5
for i in names:
    print(i)
#6
for i in numbers:
    print(i)