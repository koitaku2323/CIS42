#output.py
#Ryan Yee
#6/25/19
#Python Version: 3.7.3
#Description: Program to show output in Python

print('hello world') #single quote
print("hello world") #double quote
print("he\nllo") #\n insert a new line (same as pressing Enter)

#VARIABLES are named storage locations for numbers, strings, lists
#STRING is anything enclosed in quotes "Hello World", that's a string
#NUMBERS can be either a FLOAT (EX:9.3) or an INTEGER (Ex: 9.0)
#LISTS are things like [1,2,3] or ["Ryan", "Stoykov"]
myName= "Ryan" # declare/initialize string variable myName
Weight= 118.2333 # declare/initialize float variable Weight
Age= 16 # declare/initialize int variable Age 
Grades= [100,99,98]
nameZ= ["Ryan", "Yee"]

print ("Hello ",myName)
print ("Your weight is ",Weight, "and your age is ", Age)
print ("Your weight is %.2f and your age is %i" %(Weight,Age))
print ("Lists: grades =",Grades,"nameZ=",nameZ)
print ("This is how you print", end=' ')
print ("on the same line"

'''
>>> 
============ RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/output.py ============
hello world
hello world
he
llo
Hello  Ryan
Your weight is  118.2333 and your age is  16
Your weight is 118.23 and your age is 16
Lists: grades = [100, 99, 98] nameZ= ['Ryan', 'Yee']
This is how you print on the same line
>>> 
'''      
