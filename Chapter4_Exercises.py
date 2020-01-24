# Chapter 4. Python for Everyone
# Name: Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 22/01/2020
# Encoding: UTF-8

# 6. Rewrite gross payment as a function (`computepay`) with two arguments
# (`hours` and `rate`)
# 4.6 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay should be the normal rate for hours up to 40 and
# time-and-a-half for the hourly rate for all hours worked above 40 hours. Put
# the logic to do the computation of pay in a function called computepay() and
# use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should
# be 498.75). You should use input to read a string and float() to convert the
# string to a number. Do not worry about error checking the user input unless
# you want to - you can assume the user types numbers properly. Do not name your
# variable sum or use the sum() function.
def computepay() :
    hours = input('Enter hours:')
    rate = input('Enter rate:')
    try :
        hours = float(hours)
        rate = float(rate)
    except :
        print('Error, please enter numeric input')
        quit()

    if hours > 40 :
        pay = (rate * 40) + (1.5 * rate * (hours - 40))
    else :
        pay = rate * hours
    return print(pay)

computepay()

# 7. Rewrite grade program as a function (`computegrade`) that take a score as
# its input and returns a grade as a string.

def computegrade() :
    score = input('Enter score:')
    try :
        score = float(score)
    except :
        score = -1

    if not (score >= 0 and score <= 1) :
        print('Bad score')
    elif score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    else :
        print('F')
