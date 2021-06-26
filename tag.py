# importing stuff
import math
import turtle
import time
# making the screen
wn = turtle.Screen()
wn.title('Boring game')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)
# the runner
runner = turtle.Turtle()
runner.goto(0, 0)
x = 1
# the tagger
chaser = turtle.Turtle()
chaser.goto(0, -30)
# making the defult position up
chaser.setheading(90)
runner.setheading(90)

# settings for the turtles
runner.speed(0)
runner.shape('square')
runner.color('white')
runner.penup()
chaser.speed(0)
chaser.shape('square')
chaser.color('white')
chaser.penup()
# changing directions
def up():
    runner.setheading(90)
def down():
    runner.setheading(270)
def left():
    runner.setheading(180)
def right():
    runner.setheading(0)
def upc():
    chaser.setheading(90)
def downc():
    chaser.setheading(270)
def leftc():
    chaser.setheading(180)
def rightc():
    chaser.setheading(0)
def quit_game():
    wn.bye()
# keyboard presses
wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(upc, 'w')
wn.onkey(downc, 's')
wn.onkey(leftc, 'a')
wn.onkey(rightc, 'd')
wn.onkey(quit_game, 'q')
# collision checker
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
start = time.time()
# keeps everything running
while True:
    # kinda like wn.mainloop()
    wn.update()
    # setting the runner speed
    runner.forward(x)
    chaser.forward(1)
    # checking collisions
    if runner.ycor() > 278:
        time.sleep(1)
        runner.goto(0, 0)
        chaser.goto(0, -50)
        x += 1
        start = time.time()

    if runner.ycor() < -278:
        time.sleep(1)
        runner.goto(0, 0)
        chaser.goto(0, -50)
        x += 1
        start = time.time()

    if runner.xcor() > 278:
        time.sleep(1)
        runner.goto(0, 0)
        chaser.goto(0, -50)
        x += 1
        start = time.time()


    if runner.xcor() < -278:
        time.sleep(1)
        runner.goto(0, 0)
        chaser.goto(0, -50)
        x += 1
        start = time.time()

    if chaser.ycor() > 278:
        chaser.goto(0, 0)

    if chaser.ycor() < -278:
        chaser.goto(0, 0)

    if chaser.xcor() > 278:
        chaser.goto(0, 0)


    if chaser.xcor() < -278:
        chaser.goto(0, 0)

    # if the runner gets caught 8 times...
    if x >= 8:
        runner.write('Runner lost', align='center', font=('Courier', '30', 'bold'))
        time.sleep(5)
        wn.bye()

    if isCollision(chaser, runner):
        time.sleep(1)
        runner.goto(0, 0)
        chaser.goto(0, -50)
        x+=1
        start = time.time()

    # gives the chaser 40 seconds to catch the runner
    if (time.time() - start) >= 40:
        chaser.write('Chaser lost', align='center', font=('Courier', '30', 'bold'))
        time.sleep(5)
        wn.bye()
