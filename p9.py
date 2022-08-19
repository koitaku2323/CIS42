# p9.py
# Ryan Yee
# 7/1/19
# Python 3.7.3
# Description:  a program to compute a person's height & print out a message

feet = float(input ("Please enter the number of feet: "))
inch = float(input ("Please enter the number of inch: "))
inches = feet*12
total = inches + inch
print ( feet, "feet", inch, "inch(es) = ", total)
if (total > 72):
    print("You're tall.")
if (total > 5*12 and total < 6*12):
    print("You're average.")
if (total < 60):
    print("You're not tall.")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p9.py ==============
Please enter the number of feet: 6
Please enter the number of inch: 6
6.0 feet 6.0 inch(es) =  78.0
You're tall.
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p9.py ==============
Please enter the number of feet: 5
Please enter the number of inch: 5
5.0 feet 5.0 inch(es) =  65.0
You're average.
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p9.py ==============
Please enter the number of feet: 4
Please enter the number of inch: 4
4.0 feet 4.0 inch(es) =  52.0
You're not tall.
>>> 
'''





