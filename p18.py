#p18.py
#Ryan Yee
#7/11/19
#Python Version: 3.7.3
#Description: a program which calculates exactly how
#much more (or less) you can make with the penny on day 30.



penny = 0.01*(2)**(30)
million = 10000
difference =  penny - million
for penny in range(0,30,1):
    print("day ",penny+1,"   value:",0.01*(2)**(penny+1))
print("A penny which doubles it's value over 30 days, makes ", difference, "dollars more than A million dollars.")
'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p18.py ==============
day  1    value: 0.02
day  2    value: 0.04
day  3    value: 0.08
day  4    value: 0.16
day  5    value: 0.32
day  6    value: 0.64
day  7    value: 1.28
day  8    value: 2.56
day  9    value: 5.12
day  10    value: 10.24
day  11    value: 20.48
day  12    value: 40.96
day  13    value: 81.92
day  14    value: 163.84
day  15    value: 327.68
day  16    value: 655.36
day  17    value: 1310.72
day  18    value: 2621.44
day  19    value: 5242.88
day  20    value: 10485.76
day  21    value: 20971.52
day  22    value: 41943.04
day  23    value: 83886.08
day  24    value: 167772.16
day  25    value: 335544.32
day  26    value: 671088.64
day  27    value: 1342177.28
day  28    value: 2684354.56
day  29    value: 5368709.12
day  30    value: 10737418.24
A penny which doubles it's value over 30 days, makes  10727418.24 dollars more than A million dollars.
>>> 
'''
