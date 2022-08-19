# p11.py
# Ryan Yee
# 7/3/19
# Python 3.7.3
# Description:  a program to determine if the user can vote.

Age = float(input("How old are you? Answer: "))
Citizen = (input("Are you a U.S citizen? Answer: "))
Registeration = (input("Have you registered to vote? Answer: "))

if (Age < 18):
   print("You are not old enough to vote")
if (Citizen == "no"):
   print("You must be a citizen to vote")
if (Registeration == "no"):
   print("You must register to vote")
else:
   print("Congratulation, you can vote")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p11.py ==============
How old are you? Answer: 20
Are you a U.S citizen? Answer: yes
Have you registered to vote? Answer: yes
Congratulation, you can vote
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p11.py ==============
How old are you? Answer: 17
Are you a U.S citizen? Answer: no
Have you registered to vote? Answer: no
You are not old enough to vote
You must be a citizen to vote
You must register to vote
>>> 
'''
