import math
def paint_can_calc(width = 4 , height = 5, coverage = 5):
    x = (width * height) / coverage
    x = math.ceil(x)
    print(f'you need {x} paint cans')

paint_can_calc()