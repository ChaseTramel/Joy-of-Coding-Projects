# A program to average the grades of the user and output the average if they had increase their grade by 25%
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

gradeList = []
scope = 5
increasePercentage = .25
total = 0
increasedTotal = 0

## NOTE: this program assumes that one cannot be assigned a grade higher than 100%
## Thus, I have included error handling as follows.

for i in range(scope):
    currentGrade = float(input("Please enter a grade: "))
    if currentGrade >= 100:
        currentGrade = 100
    gradeList.append(currentGrade)
    total += float(currentGrade)
print("Current average: " + str(total/scope))

for j in range(scope):
    startingGrade = float(gradeList[j])
    if (startingGrade * (1 + increasePercentage)) >= 100:
        gradeList[j] = 100
        increasedTotal += 100
    else:
        gradeList[j] = startingGrade * (1 + increasePercentage)
        increasedTotal += gradeList[j]
print("Improved Grades: " + str(increasedTotal/scope))