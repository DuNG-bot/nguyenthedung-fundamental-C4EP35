def hello ():
    for i in range (3):
        print('Hello')


def total (a,b):
    print('Tong cua hai so la:',a+b)


##### Turtle square:

from turtle import*
def draw_square (l,c):
    import turtle
    shape('turtle')
    color(c)
    for i in range (4):
        forward(l)
        left(90)
    

for i in range (30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()

#### Turtle star:

from turtle import*
def draw_star(x,y,length):
    setpos(x,y)
    for i in range (5):
        forward(length)
        right(144)

speed(0)
color('blue')
for i in range (100):
    import random
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(3,10)
    draw_star(x,y,length)

