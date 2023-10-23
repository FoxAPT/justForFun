#Paint Coverage Calculator

import math

#Define function.
def paint_calc(height, width, cover):
    #Calculations to determine answer.
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


#Call function defined above.
paint_calc(height=test_h, width=test_w, cover=coverage)

