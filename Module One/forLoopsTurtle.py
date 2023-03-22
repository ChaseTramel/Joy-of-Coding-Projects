# A program to create a triangle with a for loop
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws


import turtle
turtle.color("blue")

size = 100
# Repeat 3 times
for i in range(3):
    turtle.forward(size)
    turtle.left(120)

turtle.Screen().exitonclick()