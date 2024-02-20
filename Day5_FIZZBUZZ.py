#create loop
top = input("how long are we fizzbuzzing till? (enter number)")
top = int(top)
for n in range(1,top + 1):
    #logic for fizz
    if n % 3 == 0:
        n = 'fizz'
    #logic for buzz
    elif n % 5 == 0:
        n = 'buzz'
    #logic for fizzbuzz
    elif n % 3 == 0 and n % 5 ==0:
        n = 'fizzbuzz'
    else:
        n = n
    print(n)


