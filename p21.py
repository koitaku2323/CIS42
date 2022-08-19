#p21.py
#Ryan Yee
#7/11/19
#Python Version: 3.7.3
#Description: a Dice Game program that generates two random dice values
#between 1 and 6 for you, and 2 for the computer.

from random import randint

while True: # loop goes on forever
    d1 = randint(1,6)
    d2 = randint(1,6)

    keep = input("You rolled %i and %i for a total of %i, keep y/n:" %(d1,d2,d1+d2))
    if keep == 'y':
        break # until the user enters a letter 'y'

pc1 = randint(1,6)
pc2 = randint(1,6)
print("The computer rolled %i and %i for a total of %i ." %(pc1,pc2,pc1+pc2))
# check winner
if pc1 + pc2 > d1 + d2:
    print("Computer wins!")
elif pc1 + pc2 < d1 + d2:
    print("You win!")
else:
    print("Tied!")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p21.py ==============
You rolled 6 and 3 for a total of 9, keep y/n:y
The computer rolled 1 and 2 for a total of 3 .
You win!
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p21.py ==============
You rolled 3 and 4 for a total of 7, keep y/n:y
The computer rolled 4 and 6 for a total of 10 .
Computer wins!
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p21.py ==============
You rolled 1 and 6 for a total of 7, keep y/n:y
The computer rolled 4 and 3 for a total of 7 .
Tied!
>>> 
'''
                 
