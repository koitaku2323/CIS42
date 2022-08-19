#p29.py
#Ryan Yee
#7/19/19
#Python Version: 3.7.3
#Description: a function named isTriangle that takes three integers as
#arguments, and that returns either True or False, depending on whether
#you can or cannot form a triangle from sticks with the given lengths.

def Triangle(a,b,c):
    print("The triangle with sides %i, %i and %i can form a triangle:" %(a,b,c), end = ' ')
    if a >= b+c or b >= a+c or c >= b+a:
       print("False")
    else:
        print("True")

def main():

    Triangle(3,4,7)
    Triangle(5,6,10)

main()

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p29.py ==============
The triangle with sides 3, 4 and 7 can form a triangle: False
The triangle with sides 5, 6 and 10 can form a triangle: True
>>>
'''

    
