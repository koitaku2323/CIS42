# p8.py
# Ryan Yee
# 6/28/19
# Python 3.7.3
# Description:a program to compute the circumference and area of a circle.

radius = float( input("Please enter the radius of the circle: "))
PI = 3.1415
circumference = radius*2*PI
area = radius**2*PI

print("A circle with radius ", radius, "inches has: ")
print("circumference: ", circumference, "inches")
print("area: ", area, "inches")
'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p8.py ==============
Please enter the radius of the circle: 12
A circle with radius  12.0 inches has: 
circumference:  75.396 inches
area:  452.37600000000003 inches
>>>
'''
