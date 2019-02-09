#!/usr/bin/env python3
fahrenheit = 0
print("Fahrenheit, Cel")
while fahrenheit <= 250:
    cel = (fahrenheit - 32) / 1.8
    print("{:5d} {:10.2f}".format(fahrenheit, cel))
    fahrenheit += 25
