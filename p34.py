#p34.py
#Ryan Yee
#7/24/19
#Python Version: 3.7.3
#Description: a program that asks the user to enter a sentence.
#1) count how many words are in the sentence 
#2) show the last word of the sentence
#3) ask the user to enter their own word, and count how many times their word
#appears in the sentence

sentence = input("Please enter a sentence:")
words = sentence.split()
print('words = ', words)


first = words[0]
print("There are",len(words),"words in this sentence.")
last = words[len(words)-1]
print("The last word of the sentence is: ",last)
print("The first word of the sentence is: ",first)

word = input('Please enter the word to be counted: ')
count = 0
for i in range(0,len(words),1):
    if words[i] == word:
        count += 1

print('The word [', word, '] appears', count, 'times')

'''
>>> 
============== RESTART: C:/Users/Ryan Yee/Desktop/CSIS42/p34.py ==============
Please enter a sentence:one two three
words =  ['one', 'two', 'three']
There are 3 words in this sentence.
The last word of the sentence is:  three
The first word of the sentence is:  one
Please enter the word to be counted: two
The word [ two ] appears 1 times
>>>
'''
