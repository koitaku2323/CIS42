#p16.py
#Ryan Yee
#7/9/19
#Python Version: 3.7.3
#Description: a program that computes the tuition in ten years and
#displays a table of the years and tuition costs.

print("Cost of Tuition at a University")
print("Year  1    Tuition  10000")
for lb in range(0,9,1):
    print("Year ",lb+2,"   Tuition ",10000*(1+0.05)**(lb+1))

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p16.py ==============
Cost of Tuition at a University
Year  1    Tuition  10000
Year  2    Tuition  10500.0
Year  3    Tuition  11025.0
Year  4    Tuition  11576.250000000002
Year  5    Tuition  12155.062500000002
Year  6    Tuition  12762.815625000003
Year  7    Tuition  13400.956406250005
Year  8    Tuition  14071.004226562505
Year  9    Tuition  14774.55443789063
Year  10    Tuition  15513.282159785162
>>>
'''
