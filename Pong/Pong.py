# module for graphics
import turtle

# Creating a window with the method of the module
window = turtle.Screen()

# Characteristics of the graphic window that will be created
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # Manage updating of the screen

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

# Main game loop
while True:
    window.update()




