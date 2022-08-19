#p19.py
#Ryan Yee
#7/11/19
#Python Version: 3.7.3
#Description: a program that uses a loop to
#display the characters in the ASCII character table from ! to ~.

count = 0
for asciiValue in range(33,127,1):
        print(chr(asciiValue), end = ' ')# shows characters on the same line
        count = count + 1 # count every character shown
        if count == 10:
           print() 
           count = 0
'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p19.py ==============
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
>>>
'''
