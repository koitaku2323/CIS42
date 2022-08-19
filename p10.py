# p10.py
# Ryan Yee
# 7/1/19
# Python 3.7.3
# Description:  a program which asks the user for a student's grade as a
# percent, and then returns their letter grade.

grade = float(input("Please enter a grade in percent: "))

if(grade >= 90):
   print("You have an 'A'.")
if(grade >= 80 and grade < 90):
   print("You have a 'B'.")
if(grade >= 70 and grade < 80):
   print("You have a 'C'.")
if(grade >= 60 and grade < 70):
   print("You have a 'D'.")
if(grade < 60):
   print("You have a 'F'.")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p10.py ==============
Please enter a grade in percent: 90
You have a 'A'.
>>> 
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p10.py ==============
Please enter a grade in percent: 80
You have a 'B'.
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p10.py ==============
Please enter a grade in percent: 70
You have a 'C'.
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p10.py ==============
Please enter a grade in percent: 60
You have a 'D'.
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p10.py ==============
Please enter a grade in percent: 50
You have a 'F'.
>>>
'''
