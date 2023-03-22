# A program that calculates and prints the average of 10 numbers
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

numbers = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    numbers[i] = input("Input a number.")

print("You entered the following numbers:")    
for j in numbers:
    print(j)

sumOfList = 0
for j in numbers:
    sumOfList += float(j)
average = sumOfList / len(numbers)
print("The average of your numbers is " + str(average))