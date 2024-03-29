# A Python program that generates a random string and compares it to a goal string input by the user, usually as Shakespeare quote, thus infinite monkeys
# The program keeps letters that are in the correct spaces, generating only randoms letters for the remaining spaces. This increases the likelihood of success each time.
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseTramel

import string
import random

def generateGuess(length):
    letters = string.printable  #a string of all printables chars, including punctuation
    testList = [""] * length  # init testList as list of empty strings goalList long
    global guesses
    guesses += 1
    global correctGuess
    print("Monkey says I know these are right:", "".join(correctGuess))
    for i in range(length):  
        if correctGuess[i] == "":
            testList[i] = random.choice(letters) # if correctGuess has a no correct letter, guess one
        else:
            testList[i] = correctGuess[i]  # otherwise, if correctGuess has a correct letter, use that correct letter
    print("Monkey says I'll guess this:", "".join(testList))
    return testList

def compareGuess(test, goal, correctGuess, guesses):
    correctLetters = 0
    for j in range(len(test)):
        if test[j] == goal[j]:  #if test list letter is correct
            correctLetters += 1  #count the correct letter
            if correctGuess[j] == "": correctGuess[j] = test[j]  # if the correct guess is empty and the test list item is correct, assign the correct guess to that list
    currentScore = round(correctLetters / len(goal), 2)
    print("Computer says you guessed " + str(correctLetters) + " correct letter(s) out of " + str(len(goal)) + "." )
    print("Computer says your guess is " + str(round(currentScore * 100)) + " percent accurate.")
    if currentScore < 1: print("Computer says you have guessed " + str(guesses) + " times.")
    trackScore(currentScore)  # use this function to update best
    return correctGuess

def trackScore(current):
    global best
    if current > best: best = current 

quote = input("Computer says what Shakespeare quote do you want the monkey to guess? ") #more complex quotes will take more time
goalList = list(quote) # init as a list of each letter
length = len(goalList)

correctGuess = ["" for _ in goalList] # init correctGuess as a list of empty strings as global variable
print(correctGuess)

best = 0
guesses = 0

while best != 1:
    correctGuess = compareGuess(generateGuess(length), goalList, correctGuess, guesses) # correct guess gets the output of compareString
print("Computer says congratulations Monkey, you guessed '" + quote + "' correctly after " + str(guesses) + " guesses.")
print("Monkey celebrates!")
