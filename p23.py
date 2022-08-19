#p23.py
#Ryan Yee
#7/16/19
#Python Version: 3.7.3
#Description: a program that generates X random integers between 20 to 50. 
#X is also a random number between 10 to 15.
#Calculate and show the smallest, largest, sum, and average of those numbers.

from random import randint

X = randint(10,15)
print( 'This program is going to generate', X , 'numbers from 20 to 50.')
sum = 0
for i in range(0, X, 1):

    number = randint(20,50)
    sum += number #add every number to the sum
    print(number, end =',')

    #first random number is when i ==0
    if i == 0: #if it is the first number
        smallest = number

    else: #if it is any number after the first
        if number < smallest: # if any number is smaller
            smallest = number # that is your new smallest

    if i == 0: #if it is the first number
        greatest = number

    else: #if it is any number after the first
        if number > greatest: # if any number is greater
            greatest = number # that is your new greatest

print('\nSmallest =' , smallest)
print('Greatest =' , greatest)
print('Sum =', sum)
print('Average =', sum/X)

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p23.py ==============
This program is going to generate 11 numbers from 20 to 50.
40,47,39,48,41,30,24,43,24,42,28,
Smallest = 24
Greatest = 48
Sum = 406
Average = 36.90909090909091
>>>
'''
            
