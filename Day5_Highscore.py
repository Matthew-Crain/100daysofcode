#get scores
scores = input("please enter scores seperated by spaces\n").split()
for n in range(0,len(scores)):
    scores[n] = int(scores[n])
#loop through scores
    topscore = 0
    for score in scores:
        if int(score) > int(topscore):
            topscore = score
            
print(f'topscore is {topscore}')

