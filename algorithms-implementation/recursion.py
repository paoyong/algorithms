from random import randint

def output(target, x = 0):
    print("hi" + str(x))
    if (x != target):
        return output(target, x + 1)
    else:
        return 0

output(randint(0, 100))
