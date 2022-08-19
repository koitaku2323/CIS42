#p27.py
#Ryan Yee
#7/19/19
#Python Version: 3.7.3
#Description: a function named isDivisible that takes two integers,
#n and m and returns true if n is evenly divisible by m and false
#otherwise.

def isDivisible(num1,num2):
    if num1%num2==0:
       print("%i is evenly divisible by %i." %(num1,num2))
    else:
       print("%i is NOT evenly divisible by %i." %(num1,num2))

isDivisible(4,2)
isDivisible(5,2)

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p27.py ==============
4 is evenly divisible by 2.
5 is NOT evenly divisible by 2.
>>>
'''
