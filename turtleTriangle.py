# A program to draw a triangle without loops using the turtle library
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import turtle

turtle.color("Yellow")

small = 25
angle = 120

turtle.forward(small)
turtle.left(angle)
turtle.forward(small)
turtle.left(angle)
turtle.forward(small)
turtle.left(angle)

turtle.Screen().exitonclick()