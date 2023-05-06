# A program that to demonstrate understanding of strings, lists, and while loops
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

firstList = [0, 1, 2, -2, -3, -4, 3, 4]
secondList = ["HELLO", "goodbye", "1234 Oooh!"]

def average_neg_evens(list):
    negEvens = []
    i = 0
    while i < len(list):
        if list[i] < 0 and i % 2 == 1:
            negEvens.append(list[i])
        i += 1
    total = 0
    for j in range(len(negEvens)):
        total += negEvens[j]
    return total / len(negEvens)

def count_letter(list):
    k = 0
    count = 0
    while k < len(list):
        count += list[k].count("o")
        count += list[k].count("O")
        k += 1
    return count

print("The average of the negative evens: " + str(average_neg_evens(firstList)))
print("There are this many Os: " + str(count_letter(secondList)))