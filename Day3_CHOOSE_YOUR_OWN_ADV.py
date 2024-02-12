print('welcome to treasure island argh, lets find the treasure')
choice1 = input('do you want to go left or right?')

if choice1 == 'left':
    choice2 = input('You come to the edge of a lake with an island in the middle, a sign says a boat will come soon do you wait or swim?')
else:
     print('you werent watching your step and walked into an open lions mouth. GAME OVER')
     exit();


if choice2 == 'wait':
    choice3 = input('You arrived at the island, there is a hut with 3 doors red, blue, and yellow, which do you choose?')
else:
    print('You were eaten by sharks. GAME OVER')
    exit()
    
if choice3 == 'red':
    print('fire erupts from the door burning you alive. GAME OVER')
    exit()
elif choice3 == 'blue':
    print('an arrow flies out striking you in the heart. GAME OVER')
    exit()
else:
    print('you open the yellow door and find a lot of gold. YOU WIN')
    exit()