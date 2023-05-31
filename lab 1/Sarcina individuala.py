# Varianta 1 din sarcina individuală
import math
import numpy as np # abbreviation

# function that help to find the z value, that will be used in find_v function
def find_z(x, y, c):
    return (c / math.pow(math.sin(x - math.pi / 3), 4)) / ((1 / 7) + math.log(math.pow(complex(y).real, 2)))
# we used complex number to solve the problem of log that is not working with negative numbers

# function that help to calculate the v value
def find_v(x, y, c):
    return (c + math.pow(find_z(x, y, c), 2)) / (3 + math.pow(find_z(x, y, c), 3) / 5)


y = -0.570
c = 1.8
# create a for that will work in a range with float numbers, and for their value , a specific output will be printed to the screen
for x in np.arange(0.345, 7.45, 0.1):
    print(f"X = {x} | Y = {y} | C = {c} | Result : {find_v(x, y, c)}")

