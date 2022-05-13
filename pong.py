import turtle

wn = turtle.Screen()
wn.title('Random Game')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Padde_a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle_b


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.2
Ball.dy = -0.2


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# KeyBind
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    Ball.setx(Ball.xcor()  + Ball.dx)
    Ball.sety(Ball.ycor()  + Ball.dy)
    
    # Top and bottom
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        
    
    elif Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        

    # Left and right
    if Ball.xcor() > 350:

    
        Ball.goto(0, 0)
        Ball.dx *= -1

    elif Ball.xcor() < -350:

        Ball.goto(0, 0)
        Ball.dx *= -1

    # Paddle and Ball collisions
    if Ball.xcor() < -340 and Ball.ycor() < paddle_a.ycor() + 50 and Ball.ycor() > paddle_a.ycor() - 50:
        Ball.dx *= -1 
    
    elif Ball.xcor() > 340 and Ball.ycor() < paddle_b.ycor() + 50 and Ball.ycor() > paddle_b.ycor() - 50:
        Ball.dx *= -1
    
