# Chapter 3. Python for Everyone
# Name: Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 22/01/2020
# Encoding: UTF-8

# 1. Rewrite gross payment to give 1.5 times the hourly rate for hours worked
# above 40 hours.
hours = input('Enter hours:')
hours = float(hours)
rate = input('Enter rate:')
rate = float(rate)

if hours > 40 :
    pay = (rate * 40) + (1.5 * rate * (hours - 40))
else :
    pay = rate * hours

print('Pay:', pay)

# 2. Rewrite to exit gracefully when input error happens.
hours = input('Enter hours:')
rate = input('Enter rate:')
try :
    hours = float(hours)
    rate = float(rate)
    if hours > 40 :
        pay = (rate * 40) + (1.5 * rate * (hours - 40))
    else :
        pay = rate * hours
    print('Pay:', pay)
except :
    print('Error, please enter numeric input')

# 3. Score between 0 and 1
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
