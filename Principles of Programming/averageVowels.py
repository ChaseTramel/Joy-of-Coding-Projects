# A program that takes a list of strings and return the average number of vowels per string
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

vowels = ["a", "e", "i","o", "u", "y"]

def averageVowels(list):
    vowelCount = 0
    for i in list:
        for j in vowels:
            vowelCount += i.count(j)
    return(vowelCount / len(list))

exampleList = ["Zebra", "lightsaber", "1234 JOYS!", "This is a test."]
print(averageVowels(exampleList))