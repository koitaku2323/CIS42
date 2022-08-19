# p13.py
# Ryan Yee
# 7/3/19
# Python 3.7.3
# Description: a program to convert any given number of total cents (under 100)
# into the correct number of: quarters, dimes, nickels, pennies.

cents = int(input("Please enter the number of cents: "))
quarters = int(cents/25)
cents2 = cents - quarters*25
dimes = int(cents2/10)
cents3 = cents2 - dimes*10
nickels = int(cents3/5)
cents4 = cents3 - nickels*5
pennies = int(cents4/1)
cents5 = cents4 - pennies*1
total1 = quarters*25
total2 = dimes*10
total3 = nickels*5
total4 = pennies*1
print("# of Quarters:", end = " ")
print(quarters, end = " ")
print("x 25c =", end = " ")
print(total1, end = " ")
print("cents total")
print("# of Dimes:", end = " ")
print(dimes, end = " ")
print("x 10c =", end = " ")
print(total2, end = " ")
print("cents total")
print("# of Nickels:", end = " ")
print(nickels, end = " ")
print("x 5c =", end = " ")
print(total3, end = " ")
print("cents total")
print("# of Pennies:", end = " ")
print(pennies, end = " ")
print("x 1c =", end = " ")
print(total4, end = " ")
print("cents total")

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p13.py ==============
Please enter the number of cents: 66
# of Quarters: 2 x 25c = 50 cents total
# of Dimes: 1 x 10c = 10 cents total
# of Nickels: 1 x 5c = 5 cents total
# of Pennies: 1 x 1c = 1 cents total
>>>
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p13.py ==============
Please enter the number of cents: 99
# of Quarters: 3 x 25c = 75 cents total
# of Dimes: 2 x 10c = 20 cents total
# of Nickels: 0 x 5c = 0 cents total
# of Pennies: 4 x 1c = 4 cents total
>>> 
'''
