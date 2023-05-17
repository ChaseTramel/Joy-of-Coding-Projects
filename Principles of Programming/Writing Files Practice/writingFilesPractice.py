# A program to practice reading and writing in files
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import os

def printWithDash(filepath):
    print("test")
    with open(filepath, 'r') as file:
        for line in file:
            print("-" + line.rstrip())

def outputNumbers():
    name = input("What should we name the file?") + ".txt"
    print("Okay, we will name the file " + name)
    with open(name , 'w') as file:
        while True:
            newNumber = input("Enter a number. Enter zero to quit. ")
            if newNumber == '0':  # Compare with a string
                return
            else:
                file.write(newNumber + "\n")

def countLinesWords(filepath):
    fileName = os.path.basename(filepath)
    with open(filepath, "r") as file:
        lineCount = 0
        wordCount = 0
        for line in file:
            lineCount += 1
            words = line.split()
            for j in words:
                wordCount += 1
        printCounts(fileName, lineCount, wordCount)
    

def printCounts(name, lineCount, wordCount):
    output = name + ": " + str(lineCount) + " lines, " + str(wordCount) + " words"
    with open("counts.txt", "a") as file:
        file.write(output + "\n")
    print(output)

printWithDash("Module One/Writing Files Practice/add.txt")

files = ["Module One/Writing Files Practice/text1.txt", "Module One/Writing Files Practice/text2.txt", "Module One/Writing Files Practice/text3.txt"]
for i in files:
    countLinesWords(i)

outputNumbers()