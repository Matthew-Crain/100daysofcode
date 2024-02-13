import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.randint(0,2)
choice = int(input("Do you want to play Rock(0),Paper(1), Or Scissors(2)?\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print('that is not a valid choice please try again')
    exit()

print('VS')

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and computer == 2:
    print ('YOU WIN')
elif computer == 0 and choice ==2:
    print ('YOU LOSE')
elif choice > computer:
    print('YOU WIN')
elif choice == computer:
    print('ITS A DRAW')
else:
    print('YOU LOSE')
