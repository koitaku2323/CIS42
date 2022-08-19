# p12.py
# Ryan Yee
# 7/3/19
# Python 3.7.3
# Description: a program to simulate rock-paper-scissors game.

player1 = float(input("Enter Rock(1), Paper(2) or Scissors(3)\nPlayer1: "))
import random
randomNum = random.randint(1,3)
print("player2:", end = " ")
print(randomNum)

if (player1 == 1 and randomNum == 1):
    print("Result: Tie!")
if (player1 == 1 and randomNum == 2):
    print("Result: Player 2 wins,Paper covers rock!")
if (player1 == 1 and randomNum == 3):
    print("Result: Player 1 wins, Rock breaks Scissors!")
if (player1 == 2 and randomNum == 1):
    print("Result: Player 1 wins, Paper covers rock!")
if (player1 == 2 and randomNum == 2):
    print("Result: Tie!")
if (player1 == 2 and randomNum == 3):
    print("Result: Player 2 wins, Scissors cut paper!")
if (player1 == 3 and randomNum == 1):
    print("Result: Player 2 wins, Rock breaks Scissors!")
if (player1 == 3 and randomNum == 2):
    print("Result: Player 1 wins, Scissors cut paper!")
if (player1 == 3 and randomNum == 3):
    print("Result: Tie!")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p12.py ==============
Enter Rock(1), Paper(2) or Scissors(3)
Player1: 1
player2: 1
Result: Tie!
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p12.py ==============
Enter Rock(1), Paper(2) or Scissors(3)
Player1: 1
player2: 3
Result: Player 1 wins, Rock breaks Scissors!
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p12.py ==============
Enter Rock(1), Paper(2) or Scissors(3)
Player1: 1
player2: 2
Result: Player 2 wins,Paper covers rock!
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p12.py ==============
Enter Rock(1), Paper(2) or Scissors(3)
Player1: 2
player2: 3
Result: Player 2 wins, Scissors cut paper!
>>> 
'''
