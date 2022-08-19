#p17.py
#Ryan Yee
#7/9/19
#Python Version: 3.7.3
#Description:a program that reads in X whole numbers and outputs
#(1) the sum of all positive numbers,
#(2) the sum of all negative numbers, and
#(3) the sum of all positive and negative numbers.

def main():
    X = int(input("How many numbers would you like to enter?"))

    Sum = 0
    sumNeg = 0
    sumPos = 0
    for index in range(0,X,1):
        number = float(input("Enter number %i :" %(index+1) ))

        # add every number to Sum
        Sum = Sum + number # Sum += number

        # only add negative numbers to sumNeg
        if number < 0:
            sumNeg += number # sumNeg = sumNeg + number

        if number >= 0:
            sumPos += number

    
    print("Sum=", Sum)
    print("sumNeg=", sumNeg)
    print("SumPos=", sumPos)

while True:
    main()
    if input("Do you want to repeat(y/n)") == 'n' :
        break
'''
>>> 
============== RESTART: C:\Users\Ryan Yee\Desktop\CSIS42\p17.py ==============
How many numbers would you like to enter?5
Enter number 1 :4
Enter number 2 :7
Enter number 3 :-5
Enter number 4 :-3
Enter number 5 :0
Sum= 3.0
sumNeg= -8.0
SumPos= 11.0
Do you want to repeat(y/n)y
How many numbers would you like to enter?4
Enter number 1 :3
Enter number 2 :2
Enter number 3 :-7
Enter number 4 :-8
Sum= -10.0
sumNeg= -15.0
SumPos= 5.0
Do you want to repeat(y/n)n
>>>
It errors because of the comment syntax
'''

