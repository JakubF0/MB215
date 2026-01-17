import turtle
import tkinter.simpledialog as simpledialog

# Set up the window
screen = turtle.Screen()
screen.title("Turtle Lab")

# Create a turtle
t = turtle.Turtle()

# Set pen size to 3
t.pensize(3)

# Set drawing color to blue
t.color("blue")

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle right by 90 degrees
t.right(90)

# Move the turtle forward by 50 units
t.forward(50)

# Turn the turtle left by 90 degrees
t.left(90)

# Lift the pen up
t.penup()

# Move the turtle to a specific location
t.goto(-50, 50)

# Put the pen down
t.pendown()

# Draw a circle with radius of 25
t.circle(25)

# Draw a dot with diameter 10
t.dot(10)

# Set the turtle heading to 0 (East)
t.setheading(0)

# Change the turtle color
t.color("red")

# Draw a filled shape
t.begin_fill()
t.forward(60)
t.left(120)
t.forward(60)
t.left(120)
t.forward(60)
t.end_fill()

# Clear the drawing
t.clear()

# Reset the turtle's state
t.reset()

# Hide the turtle
t.hideturtle()

# Display the turtle
t.showturtle()

# Set animation speed
t.speed(10)

# Display text
t.write("Hello Turtle!", font=("Arial", 14, "bold"))

# Get input with a dialog box
user_name = simpledialog.askstring("Input", "Enter your name:")

# Respond to user input
t.clear()
t.write(f"Welcome {user_name}", font=("Arial", 14, "bold"))

# Filling a shape with color
t.color("green")
t.begin_fill()
t.circle(40)
t.end_fill()

# Close the window on click
screen.exitonclick()
