# A Python program to learn how to manipulate Dictionaries
# K. Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

def count_uniq(string):
    letters = {}
    for i in string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    print(letters)
    return len(letters)


print(count_uniq("111224446"))
print(count_uniq("30444775555"))
print(count_uniq(""))