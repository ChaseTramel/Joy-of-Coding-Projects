# A program to that takes in a temperature and outputs suggestions for what the user should wear
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

def suggestion(temp):
    if temp > 90:
        return "Whoa, it’s boiling!"
    elif temp >= 80:
        return "It's getting hot"
    elif temp < 80 and temp >=60:
        return "A perfect day"
    elif temp < 60 and temp >= 32:
        return "Don't forget your sweater"
    elif temp < 32:
        return "Brr, you need a coat!"

temp = int(input("What is the temperature outside?"))
print(suggestion(temp))