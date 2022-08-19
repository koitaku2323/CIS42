# input.py
# Ryan Yee
# 6/26/19
# Python 3.7.3
# Description: Program to take input in Python

name = input ("Please enter Your Name: ") #This is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int (input ("Please enter your age (Whole number): ")) # an integer
weightKg= weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ') #end=' ' prevents new line
print ("kilograms ")

'''
>>> 
============= RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/input.py =============
Please enter Your Name: Ryan Yee
Please enter Your weight in lbs: 118
Please enter your age (Whole number): 16
Hello Human Ryan Yee your weight is
118.0 lbs
which equals = 53.52 kilograms 
>>> 
'''
