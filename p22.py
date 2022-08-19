#p22.py
#Ryan Yee
#7/16/19
#Python Version: 3.7.3
#Description: a program to let a child practice arithmetic skills.

from random import randint
while True:
    num1 = randint(0,9)
    num2 = randint(0,9)
    operation = input("Would you like to add(+),sub(-) or mul(*):")
    #ADDITION
    if operation == "+":
        answer = int(input("What is %i + %i =" %(num1,num2)))
        # ask the question again if the user is incorrect
        while answer != num1 + num2:
            answer = int(input("Incorrect, what is %i + %i =" %(num1,num2)))

    #SUBTRACTION
    if operation == "-":
        answer = int(input("What is %i - %i =" %(num1,num2)))
        # ask the question again if the user is incorrect
        while answer != num1 - num2:
            answer = int(input("Incorrect, what is %i - %i =" %(num1,num2)))

    #MULTIPLICATION
    if operation == "*":
        answer = int(input("What is %i * %i =" %(num1,num2)))
        # ask the question again if the user is incorrect
        while answer != num1 * num2:
            answer = int(input("Incorrect, what is %i * %i =" %(num1,num2)))


    repeat = input("Would you like to try again(y/n):")
    if repeat != "y":
        break

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p22.py ==============
Would you like to add(+),sub(-) or mul(*):+
What is 9 + 5 =2
Incorrect, what is 9 + 5 =3
Incorrect, what is 9 + 5 =14
Would you like to try again(y/n):y
Would you like to add(+),sub(-) or mul(*):-
What is 6 - 7 =-1
Would you like to try again(y/n):y
Would you like to add(+),sub(-) or mul(*):*
What is 5 * 9 =45
Would you like to try again(y/n):n
>>> 
'''
    
