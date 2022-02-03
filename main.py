import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create our turtle
george = turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(10)

# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# Define a function to draw and fill an equalateral right 
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()
  
# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the 
# center of the circle.
def drawFourRays(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)

# Draw and fill the front of the house
george.penup() 
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 100, 110, "white")

# Draw and fill the front door
george.penup()
george.goto(-120, -120)
george.pendown()
drawRectangle(george, 40, 60, "brown")

# Front roof
george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 100, "red")

# Side of the house
george.penup()
george.goto(-50, -120)
george.pendown()
drawParallelogram(george, 60, 110, "white")

# Window
george.penup()
george.goto(-30, -60)
george.pendown()
drawParallelogram(george, 20, 30, "grey")

# Side roof
george.penup()
george.goto(-50, -10)
george.pendown()
george.fillcolor("red")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(75)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(45)
george.end_fill()



 