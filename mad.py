# A program for learning about string manipulation
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import string

input = input("Enter a phrase!")

print(input.upper())
print(input.replace('e','x'))

def printableTest (input):
    stringInput = str(input)
    if stringInput.isprintable():
        print("'" + stringInput + "' is printable")
        return True
    else:
        print('This is not printable')    
        return False
    
printableTest(input)