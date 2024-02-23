#import libraries
import random
#create a word list
words = ["dog","cat","mouse","house","bog","hat","mat"]
#Pick a word
word = random.choice(words)
#create an input to guess a letter
guess = input("please guess a letter: ").lower
#loop through guess
for letter in word:
    if letter == guess:
        print(letter)
    else:
        print('_')


#print boolean value for correct letter placement

