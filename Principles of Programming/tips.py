## A program to predict the total cost of a meal including tax and tip
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

mealCost = 53.48
taxRate = .07
tipRate = .18

def getTotalCost (mealCost, taxRate, tipRate):
    tipCost = mealCost * tipRate
    taxCost = mealCost * taxRate
    return mealCost + tipCost + taxCost

print("$"+ str(getTotalCost(mealCost, taxRate, tipRate)))
