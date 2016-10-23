from math import cos as c
from math import pi
from math import radians as rad


while True:
    a=rad(input())
    if c(a) == 1:
        print("uguale a uno")
        break
    elif c(a) <= 1e-16:
        print("uguale a zero")
    else:
        print("falso!!!")

