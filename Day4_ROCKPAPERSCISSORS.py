import random
choice = input ('heads or tails?/n')
output = random.ranint(0,1)
if choice == output:
    print(f'you chose {choice}, the coin was {output}, YOU WIN')
else:
    print(f'you chose {choice}, the coin was {output}, YOU LOSE')