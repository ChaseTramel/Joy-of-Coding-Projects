# A python program that creates various shapes using functions and for loops
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import turtle
turtle.color("blue")

layers = 3

def rectangle(height, width):
    for i in range(4):
        if (i % 2 == 0):
            turtle.forward(width)
            turtle.left(90)
        else:
            turtle.forward(height)
            turtle.left(90)

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def cake(height, width):
    layerHeight = height / layers
    for i in range(layers):
        rectangle(layerHeight, width)
        turtle.left(90)
        turtle.forward(layerHeight)
        turtle.right(90)
    candlePosition = (width / 2) - (height / 2)
    turtle.penup()
    turtle.forward(candlePosition)
    turtle.pendown()
    triangle(height)
    return

cake(100, 300)
turtle.reset()
cake(120,205)
turtle.reset()
cake(200, 150)
turtle.reset()
cake(55, 165)


turtle.Screen().exitonclick()