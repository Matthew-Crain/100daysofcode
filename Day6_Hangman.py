#import libraries
import random
import Day6_hangman_stages
import day6_wordlist
#create a word list
#Pick a word
word = random.choice(day6_wordlist.word_list)
wordln = len(word)
#create an empty list to hold blanks
holder = []
for letters in range(len(word)):
    holder += '_'
#create while loop to allow repeatability
used_letters = []
current_lives = 6
while '_' in holder and current_lives > 0:
#create an input to guess a letter
    print(f'lives: {current_lives}')
    print(holder)
    print(Day6_hangman_stages.stages[current_lives])
    current_lives -= 1
    guess = input("please guess a letter: ").lower()
    if guess in used_letters:
        print(f'youve already used {guess} please use another letter')

    used_letters += guess
    for position in range(wordln):
        letter = word[position]
        if letter == guess:
            holder[position] = guess 
            if current_lives < 6:
                current_lives = current_lives + 1


if '_' not in holder:
    print('YOU WIN')
    print(holder)
else:
    print(current_lives)
    print(Day6_hangman_stages.stages[current_lives])
    print('YOU LOSE')
    print(holder)
    print(f'the word was {word}')
  







        


