import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Star Art")

t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)
t.hideturtle()

# ================== STAR ==================

t.color("blue")

t.penup()
t.goto(-40, -23)
t.pendown()

for _ in range(3):
    t.forward(80)
    t.left(120)

t.penup()
t.goto(-40, 23)
t.pendown()

for _ in range(3):
    t.forward(80)
    t.right(120)

# ============== FLOWER (Top Left) ==============

colors = ["red", "orange", "yellow", "green"]

t.penup()
t.goto(-150, 180)
t.setheading(0)
t.pendown()

for i in range(18):
    t.color(colors[i % 4])
    t.circle(40)
    t.right(20)

colors = ["red", "orange", "yellow", "green"]

t.penup()
t.goto(-150, -180)
t.setheading(0)
t.pendown()

for i in range(18):
    t.color(colors[i % 4])
    t.circle(40)
    t.right(20)
colors = ["red", "orange", "yellow", "green"]

t.penup()
t.goto(150, 180)
t.setheading(0)
t.pendown()

for i in range(18):
    t.color(colors[i % 4])
    t.circle(40)
    t.right(20)
colors = ["red", "orange", "yellow", "green"]

t.penup()
t.goto(150, -180)
t.setheading(0)
t.pendown()

for i in range(18):
    t.color(colors[i % 4])
    t.circle(40)
    t.right(20)
turtle.done()