import random
choice = input ('heads or tails?\n')
output = random.randint(0,1)
if output == 1:
    output = 'heads'
else:
    output = 'tails'
if choice == output:
    print(f'you chose {choice}, the coin was {output}, YOU WIN')
else:
    print(f'you chose {choice}, the coin was {output}, YOU LOSE')