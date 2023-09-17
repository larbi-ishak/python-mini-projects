import turtle

# initialize screen
wind = turtle.Screen()

# config window
wind.title("PING_PONG")
wind.bgcolor("black")
wind.setup(width=800, height=600)

# to stop window from auto update so you can control it like you want
wind.tracer(0)

# middle of the screen 0, 0 x,y like cartesian coordinates


bat1 = turtle.Turtle()
# interval to update the bat 0 is the quickest interval
bat1.speed(0)
bat1.shape("square")
# stretching the size vertical and horizontal
bat1.shapesize(stretch_wid=5, stretch_len=1)
bat1.color("blue")

# by default objects in turtle when moving drawing some line of movement behind it
# we don't want that here
bat1.penup()

# placing the bat in the max left
bat1.goto(-350, 0)

# bat2
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape("square")
bat2.shapesize(stretch_wid=5, stretch_len=1)
bat2.color("red")
bat2.penup()
bat2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

player1_score = 0
player2_score = 0
# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.goto(0, 260)
score.write(f"Player 1: {player1_score} Player 2: {player2_score} ",
            align="center", font=("Ink Free", 24, "bold"))


# Moving up down
def bat1_up():
    y = bat1.ycor()  # get y coordinates
    if y < 300:
        y += 20
        bat1.sety(y)  # update


def bat1_down():
    y = bat1.ycor()
    if y > -300:
        y -= 20
        bat1.sety(y)


def bat2_up():
    y = bat2.ycor()
    if y < 300:
        y += 20
        bat2.sety(y)


def bat2_down():
    y = bat2.ycor()
    if y > -300:
        y -= 20
        bat2.sety(y)


# keyboard Bindings
wind.listen()
wind.onkeypress(bat1_up, "d")
wind.onkeypress(bat1_down, "f")
wind.onkeypress(bat2_up, "k")
wind.onkeypress(bat2_down, "j")

# main Loop
while True:
    # update screen
    wind.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check ball to rewind when hitting the window border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1
    elif ball.xcor() < -350:
        ball.setx(-350)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat2.ycor() + 40 and ball.ycor() > bat2.ycor() - 40):
        ball.dx *= -1
        ball.dy *= -1
    # adding score when bat2 fails to hit the ball
    elif ball.xcor() > 340 and not (ball.ycor() < bat2.ycor() + 40 and ball.ycor() > bat2.ycor() - 40):
        player1_score += 1
        score.clear()
        score.write(f"Player 1: {player1_score} Player 2: {player2_score} ",
                    align="center", font=("Ink Free", 24, "bold"))
        ball.goto(0, 0)
        # checking score if more than 10 quit the game
        if player1_score >= 10:
            quit()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat1.ycor() + 40 and ball.ycor() > bat1.ycor() - 40):
        ball.dx *= -1
        ball.dy *= -1
    # adding score when bat1 fails to hit the ball
    elif ball.xcor() < -340 and not (ball.ycor() < bat1.ycor() + 40 and ball.ycor() > bat1.ycor() - 40):
        player1_score += 1
        score.clear()
        score.write(f"Player 1: {player1_score} Player 2: {player2_score} ",
                    align="center", font=("Ink Free", 24, "bold"))
        ball.goto(0, 0)
        # checking score if more than 10 quit the game
        if player1_score >= 10:
            quit()
