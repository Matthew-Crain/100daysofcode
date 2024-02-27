def primecheck(x = int(input("what number do you want to check?\n"))):
    i = 1
    counter = 0
    while i < x + 1:
        if x % i == 0:
            counter += 1
            i += 1
        else:
            counter += 0
            i += 1
    if counter == 2 or x == 1:
        print(f'{x} is a prime number, the counter is {counter}')
        exit()
    elif counter > 2:
        print(f'{x} is not a prime number, the counter is {counter}')
    


primecheck()
        