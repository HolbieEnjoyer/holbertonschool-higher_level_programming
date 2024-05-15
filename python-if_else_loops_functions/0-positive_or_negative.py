#!/usr/bin/python3
import random
number = random.randint(-10, 10)
msg = "is zero"
if (number > 0):
    msg = "is positive"
elif (number < 0):
    msg = "is negative"
print(f'{number} {msg}')
