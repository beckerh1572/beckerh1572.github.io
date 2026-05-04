# Hannah Becker
# 04/02/2026
# P4LAB1_BeckerHannah
# Draws a house using a square and triangle with loops

import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("#8fb3c1")  # light blue background

# Create turtle
t = turtle.Turtle()
t.pensize(3)
t.color("darkgreen")

# Move turtle to starting position
t.penup()
t.goto(-50, -50)
t.pendown()

# ---- Draw Square (FOR loop) ----
for i in range(4):
    t.forward(100)
    t.left(90)

# Move to top of square
t.left(90)
t.forward(100)
t.right(90)

# ---- Draw Triangle (WHILE loop) ----
t.fillcolor("forestgreen")
t.begin_fill()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

t.end_fill()

# Hide turtle and finish
t.hideturtle()
turtle.done()