#import libraries
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#create a word list
words = ["dog","cat","mouse","house","bog","hat","mat"]
#Pick a word
word = random.choice(words)
wordln = len(word)
#create an empty list to hold blanks
holder = []
for letters in range(len(word)):
    holder += '_'
#create while loop to allow repeatability
lives = 6
while '_' in holder and lives > 0:
#create an input to guess a letter
    print(f'lives: {lives}')
    print(holder)
    print(stages[lives])
    lives -= 1
    guess = input("please guess a letter: ").lower()
    for position in range(wordln):
        letter = word[position]
        if letter == guess:
            holder[position] = guess 
            lives = lives + 1

if '_' not in holder:
    print('YOU WIN')
    print(holder)
else:
    print(lives)
    print(stages[lives])
    print('YOU LOSE')
    print(holder)
    print(f'the word was {word}')
  







        


