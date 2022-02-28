# module for graphics
import turtle
import os

# Creating a window with the method of the module
window = turtle.Screen()

# Characteristics of the graphic window that will be created
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # Manage updating of the screen

# Score
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_len=1, stretch_wid=5)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_len=1, stretch_wid=5)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # Defining the amount of pixels the ball moves each time
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Movement of paddles
def paddle_1_up():
    y = paddle_1.ycor() # Save on the "y" variable the value of the Y coordinate
    y += 20 # Defining new coordinate for Y, moving up
    paddle_1.sety(y) # Setting new coordinate

def paddle_2_up():
    y = paddle_2.ycor() 
    y += 20 
    paddle_2.sety(y)   

def paddle_1_down():
    y = paddle_1.ycor() 
    y -= 20 
    paddle_1.sety(y) 

def paddle_2_down():
    y = paddle_2.ycor() 
    y -= 20 
    paddle_2.sety(y)       

# Keyboard directions
window.listen() # To obtain input from keyboard
window.onkeypress(paddle_1_up, "w") # When pressing "w" call the paddle_1_up() function    
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "8")
window.onkeypress(paddle_2_down, "2")

# Main game loop
while True:
    window.update()

    # Changing the position of the ball to create the movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking position of the ball respect the top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverses the direction of the movement
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Checking position of the ball respect to the right and left borders
    if ball.xcor() > 350:
        score_1 += 1
        pen.clear() # Reset counter
        pen.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("arial", 28, "normal"))
        ball.goto(0, 0) # Send ball back to the center
        ball.dx *= -1   

    if ball.xcor() < -350:
        score_2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("arial", 28, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1   

    # Rebound process on paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
       ball.setx(-340)
       ball.dx *= -1 

