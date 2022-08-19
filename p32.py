#p32.py
#Ryan Yee
#7/19/19
#Python Version: 3.7.3
#Description:  a function recurse(num) which calls itself until num is equal
#to zero, and shows num every time it calls itself.

def recurse(num):
    if num == 0:
        print("Program Terminated")
    else:
        print(num)
        recurse(num-1)

recurse(10)

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p32.py ==============
10
9
8
7
6
5
4
3
2
1
Program Terminated
>>>
'''
