# Chapter 1. Python for Everyone
# Name: Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 19/01/2020
# Encoding: UTF-8

## Notes

# Python reserves 35 keywords: `and`, `as`, `assert`, `break`, `class`,
# `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`,
# `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `None`, `nonlocal`,
# `not`, `or`, `pass`, `raise`, `return`, `True`, `try`,  `while`, `with`,
# `yield`, `async`, and `await`.

## Excercises

# 2. Program that welcomes
name = input('Enter your name')
print('Hello', name)

# 3. Program to compute gross pay
hours = input('Enter hours:')
rate = input('Enter rate:')
print('Pay:', float(hours) * float(rate))

# 4. Write down value and type
width = 17
height = 12.0

print('1.', width//2, type(width//2)) # 8, int.
print('2.', width/2.0, type(width/2.0)) # 8.5, float.
print('3.', height/3, type(height/3)) # 4, float.
print('4.', 1 + 2 * 5, type(1 + 2 * 5)) # 11, int.

# 5. Converts temperature
temp = input('Enter temperature in Celsius:')
print('It is', (float(temp) * 1.8) + 32, 'Farenheit degrees.')
