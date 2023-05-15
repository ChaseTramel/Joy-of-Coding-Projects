# A program to take a string from the user and finds the index of the first occurance of a letter
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

letter = "u"

def stringU():
    userSays = str(input("What say you?"))
    for i in range(len(userSays)):
        if userSays[i] == letter or userSays[i] == letter.upper():
            return i
        if i == (len(userSays) - 1):
            return "-1"

print(stringU())