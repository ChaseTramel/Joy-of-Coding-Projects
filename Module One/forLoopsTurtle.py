# A program to create a triangle with a for loop
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws


import turtle
turtle.color("blue")

# Repeat 3 times
def triangle(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()
    return

triangle(100)
triangle(50)
triangle(25)

turtle.Screen().exitonclick()