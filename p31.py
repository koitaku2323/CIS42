#p31.py
#Ryan Yee
#7/19/19
#Python Version: 3.7.3
#Description: a function isEven(num) which returns True if the value is even,
#and False otherwise.

def isEven(num):
    print("The number %i is Even:" %num, end = ' ')
    if num%2 == 0:
        print("True")
    else:
        print("False")

def main():
           isEven(22)
           isEven(33)

main()

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p31.py ==============
The number 22 is Even: True
The number 33 is Even: False
>>>
'''
