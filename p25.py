#p25.py
#Ryan Yee
#7/18/19
#Python Version: 3.7.3
#Description: a program that asks the user to input a sentence.
#The program will ask the user what two letters are to be counted.

string = str(input("Please enter a sentence:"))
print("The sentence you entered was:", string)
count1 = 0
count2 = 0
letter1 = str(input("Please enter letter 1:"))
letter2 = str(input("Please enter letter 2:"))
for i in string:
    if i == letter1:
        count1 = count1 + 1

for i in string:
    if i == letter2:
        count2 = count2 + 1

print("The letter", letter1, "occurs %i"%count1,"time(s) in this sentence.")
print("The letter", letter2, "occurs %i"%count2,"time(s) in this sentence.")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p25.py ==============
Please enter a sentence:hello world
The sentence you entered was: hello world
Please enter letter 1:h
Please enter letter 2:l
The letter h occurs 1 time(s) in this sentence.
The letter l occurs 3 time(s) in this sentence.
>>>
'''
