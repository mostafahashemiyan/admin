import random

n = random.randint(1, 99)
hads = int(input("enter a number(1,99) : "))
x = []
x = hads
while x != 5:
    if hads < n:
        print("oh , your guess is not correct")
        hads = int(input(" try again , go up : "))
    elif hads > n:
        print("oh , your guess is not correct ")
        hads = int(input(" try again , go down : "))
    else:
        print(" good job !!!")
        break
