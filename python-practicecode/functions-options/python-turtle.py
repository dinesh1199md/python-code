import turtle 

def draw_letter(letter, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    if letter == "A":
        turtle.left(60)
        turtle.forward(50)
        turtle.right(120)
        turtle.forward(50)
        turtle.backward(25)
        turtle.right(120)
        turtle.forward(25)
        turtle.penup()
        turtle.home()
    elif letter == "I":
        turtle.forward(50)
        turtle.backward(25)
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.right(180)
        turtle.pendown()
        turtle.forward(50)
    elif letter == "S":
        turtle.forward(25)
        turtle.circle(-25, 180)
        turtle.circle(25, 180)
        turtle.forward(25)
    elif letter == "H":
        turtle.forward(50)
        turtle.backward(25)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(25)
        turtle.backward(50)
    elif letter == "V":
        turtle.right(30)
        turtle.forward(50)
        turtle.backward(50)
        turtle.left(60)
        turtle.forward(50)
        turtle.backward(50)
        turtle.right(30)
    elif letter == "R":
        turtle.forward(50)
        turtle.right(90)
        turtle.circle(-12.5, 180)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(135)
        turtle.forward(35)
    elif letter == "Y":
        turtle.forward(25)
        turtle.left(60)
        turtle.forward(25)
        turtle.backward(25)
        turtle.right(120)
        turtle.forward(25)
        turtle.backward(25)
        turtle.left(60)
        turtle.backward(25)
    # Add more letters as needed

def draw_name(name):
    x_start = -200 # Starting x position
    y_start = 0 # Starting y position
    spacing = 40 # Spacing between letters
    for i, letter in enumerate(name):
        x = x_start + i * spacing
        draw_letter(letter.upper(), x, y_start)

# Customize this with your name
name = "Aishvarya"
turtle.speed(2) # Slow down the turtle to see the drawing
draw_name(name)
turtle.done()
turtle.done()