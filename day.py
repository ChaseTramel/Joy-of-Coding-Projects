# A program to for learning about string and number manipulation
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import math

favMonth = input("What's your favorite month?")
favDay = input("What's your favorite day of that month?")

titleMonth = favMonth.title()  # Make the month title case so it appears correctly later
intDay = int(favDay)

print(titleMonth + " " + str(favDay) + ", 2020")

if favMonth.isalnum():
    print("Yes, " + titleMonth + "  is alphanumberic.")
else:
    print("No, " + titleMonth + "  is not alphanumberic.")

print("There are " + str(favDay.count('2')) + " twos in " + favDay + ".") # made results of count() a string bc it's an int

print("The factorial of " + favDay + " is " + str(math.factorial(intDay)) + ".")

print("The log base of " + str(abs(intDay)) + " is " + str(math.log(abs(intDay))) + ".")