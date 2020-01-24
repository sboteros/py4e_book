# Chapter 4. Python for Everyone
# Name: Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 24/01/2020
# Encoding: UTF-8

# 1. Program that reads numbers until the user enters "done". When finishing, it
# prints out the total, count and average of numbers. Bad numbers prompt a
# message and are skipped.

total = 0
count = 0
while True :
    number = input('Enter a number: ')
    try :
        number = float(number)
    except :
        if number == 'done' :
            break
        else :
            print('Invalid input')
            continue

    total = total + number
    count = count + 1
    average = total / count
print(total, count, average)

# 2. A similar one as the last one, but it promts the maximum and minimum.

largest = None
smallest = None
while True :
    number = input('Enter a number: ')
    try :
        number = float(number)
    except :
        if number == 'done' :
            break
        else :
            print('Invalid input')
            continue

    if largest is None or largest < number :
        largest = number
    if smallest is None or smallest > number :
        smallest = number
print(largest, smallest)
