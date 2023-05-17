# A program for learning about math functions
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import math

def forceNumber(input):
    if input.isnumeric():
        input = float(input)
        print(str(input) + " can be a number.")
        print(str(abs(input)))
        print(str(math.floor(input)))
        print(str(round(input, 2)))
        return True
    else:
        print(str(input) + " can't be a number.")
        return False

forceNumber(input("Enter a number!"))