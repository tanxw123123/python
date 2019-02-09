#!/usr/bin/env python3
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = b * b - 4 * a * c
if d < 0:
    print("the value is error")
else:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
