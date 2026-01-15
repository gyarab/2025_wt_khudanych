import turtle
import math
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def domecek(a):
    uhlopricka = a * math.sqrt(2)
    
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(45)
    t.forward(uhlopricka / 2)
    t.left(90)
    t.forward(uhlopricka / 2)
    t.left(45)
    t.forward(a)
    t.left(135)
    t.forward(uhlopricka)
    t.left(135)
    t.forward(a)
    t.left(135)
    t.forward(uhlopricka)
    t.setheading(0)

def elipsa(x0, y0, a, b):
    t.penup()
    t.goto(x0 + a, y0)
    t.pendown()
    
    for stupen in range(10, 370, 10):
        rad = math.radians(stupen)
        x = x0 + a * math.cos(rad)
        y = y0 + b * math.sin(rad)
        t.goto(x, y)

def zemekoule(a):
    polomer = a / 2
    stred_x = t.xcor()
    stred_y = t.ycor() + polomer
    
    t.circle(polomer)
    
    t.penup()
    t.goto(stred_x - polomer, stred_y)
    t.pendown()
    t.goto(stred_x + polomer, stred_y)
    
    t.penup()
    t.goto(stred_x, stred_y - polomer)
    t.pendown()
    t.goto(stred_x, stred_y + polomer)
    
    elipsa(stred_x, stred_y, polomer * 0.3, polomer)
    elipsa(stred_x, stred_y, polomer * 0.6, polomer)
    
    t.penup()
    t.goto(stred_x, stred_y - polomer)
    t.setheading(0)

t.penup()
pos_x = -350
mezera = 40

for i in range(6):
    velikost = random.randint(70, 110)
    t.penup()
    
    if i % 2 == 0:
        t.goto(pos_x, 0)
        t.pendown()
        domecek(velikost)
    else:
        t.goto(pos_x + velikost / 2, 0)
        t.pendown()
        zemekoule(velikost)
        
    t.penup()
    t.forward(mezera)
    pos_x = pos_x + velikost + mezera

turtle.done()