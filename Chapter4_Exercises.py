# Chapter 4. Python for Everyone
# Name: Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 22/01/2020
# Encoding: UTF-8

# 6. Rewrite gross payment as a function (`computepay`) with two arguments
# (`hours` and `rate`)

def computepay(hours, rate) :
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
    print('Pay:', pay)

computepay(45, 10)

# 7. Rewrite grade program as a function (`computegrade`) that take a score as
# its input and returns a grade as a string.

def computegrade(score) :
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

computegrade(0.95)
computegrade('perfect')
computegrade(10.0)
computegrade('0.75')
computegrade('0.5')
