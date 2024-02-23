#import libraries
import random
#create a word list
words = ["dog","cat","mouse","house","bog","hat","mat"]
#Pick a word
word = random.choice(words)
#word output for testing
print(f'the word is: ' + word)
#create an empty list to hold blanks
holder = []
for letters in range(len(word)):
    holder += '_'

#create an input to guess a letter
guess = input("please guess a letter: ").lower()
#loop through guess

for position in range(len(word)):
    letter = word[position]
    if letter == guess:
        holder[position] = guess


print(holder)

        


