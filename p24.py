#p24.py
#Ryan Yee
#7/18/19
#Python Version: 3.7.3
#Description:1) Ask the user to enter X numbers into a list.
#2) Put those numbers into a list, and show the list.
#3) Calculate and show the sum, average, min, max of those numbers.
#4) You are not allowed to use any pre-existing python functions
#such as sample(), sum(), min(), max(), average()...unless you write them yourself.
#5) Make another list, but with double the values of the first lists

X = int(input("How many numbers would you like to enter?"))
sum = 0
for i in range(0, X, 1):
    number = int(input("Enter number %i: " %(i+1)))
    sum += number
    num2 = number*2 
    print("double the input: ", num2)
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
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p24.py ==============
How many numbers would you like to enter?4
Enter number 1: 1
double the input:  2
Enter number 2: 2
double the input:  4
Enter number 3: 3
double the input:  6
Enter number 4: 4
double the input:  8

Smallest = 1
Greatest = 4
Sum = 10
Average = 2.5
>>>
'''
