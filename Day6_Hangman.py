#import libraries
import random
#create a word list
words = ["dog","cat","mouse","house","bog","hat","mat"]
#Pick a word
word = random.choice(words)
wordln = len(word)
#word output for testing
print(f'the word is: ' + word)
#create an empty list to hold blanks
holder = []
for letters in range(len(word)):
    holder += '_'
#create while loop to allow repeatability
lives = 5
while '_' in holder and lives != 0:
#create an input to guess a letter
    print(f'lives: {lives}')
    print(holder)
    guess = input("please guess a letter: ").lower()
    lives -= 1
    for position in range(wordln):
        letter = word[position]
        if letter == guess:
            holder[position] = guess

if '_' not in holder:
    print('YOU WIN')
else:
    print('YOU LOSE')
  







        


