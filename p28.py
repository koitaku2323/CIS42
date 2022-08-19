#p28.py
#Ryan Yee
#7/19/19
#Python Version: 3.7.3
#Description:Write a function called multAdd that takes three floats(a,b,c)
#as parameters and then returns a*b+c.
#Write a main() function which starts the program, and calls the multAdd function
#giving it arguments 1,2,3

def multAdd(num1,num2,num3):
    product = num1*num2+num3
    print("%i times %i and then add %i equals:" %(num1,num2,num3), product)

def main():

    multAdd(3,4,5)

main()

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p28.py ==============
3 times 4 and then add 5 equals: 17
>>>
'''

    
