import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.goto(-50,20)
leonardo.goto(-50,-20)

michelangelo.forward(50)
leonardo.forward(50)

michelangelo.bk(100)
leonardo.bk(100)

#Race 1
michelangelo.fd(random.randrange(1,100))
leonardo.fd(random.randrange(1,100))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Race 2
for i in range (1,10):
  michelangelo.fd(random.randrange(1,10))
  leonardo.fd(random.randrange(1,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
michelangelo.down()
leonardo.down()

def shape(length = "", sides = ""):
  interior_angle = (sides-2 * 180)/sides 
  for i in range(0, sides, 1):
    michelangelo.fd(length)
    michelangelo.left(interior_angle)
  michelangelo.clear()
  
shape(50,3)
shape(50,4)
shape(50,6)
shape(50,9)
shape(50,12)


window.exitonclick()
