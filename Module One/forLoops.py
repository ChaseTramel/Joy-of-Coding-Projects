# A program to learn about for loops
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

furniture = ['table', 'chair', 'rack', 'shelf']
for item in furniture:
    print(item)
print()

for i in range(1,6):
    print(i)
print()    

for i in range(2,12,3):
    print(i)
print()

for i in range(-10, 2, 2):
    print(i, end=" ")
print()

for i in range(4):
    for j in range(4):
        print("*", end="")
    print()
print()

for i in "CSCI 150":
    print(i)
print()

for i in range(1,11):
    print(i)