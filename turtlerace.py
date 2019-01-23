import turtle as a
from random import randint


no_of_turtles=int(input("Enter the number of players in the game:"))

colors=["red","black","brown","green"]

a.setup(width=0.99, height=0.99, startx=0, starty=0)
a.penup()
a.speed(1000)
a.goto(-160,200)
a.write("Turtle Race :")
wt=a.Screen()
wt.register_shape("big",((0,0),(30,0),(30,30),(0,30)))
wt.register_shape("raja",((0,16), (-2,14), (-1,10), (-4,7),
                              (-7,9), (-9,8), (-6,5), (-7,1), (-5,-3), (-8,-6),
                              (-6,-8), (-4,-5), (0,-7), (4,-5), (6,-8), (8,-6),
                              (5,-3), (7,1), (6,5), (9,8), (7,9), (4,7), (1,10),
                              (2,14)))
a.shape("raja")

a.goto(-140,140)

for i in range(40):
    a.write(i)
    a.right(90)
    a.forward(10)

    for ii in range(10):
        a.pendown()
        a.forward(20)
        a.penup()
        a.forward(10)

    a.forward(-310)
    a.left(90)
    a.forward(20)

turtle_obj=[]

for i in range(no_of_turtles):
    turtle_obj.append(a.Turtle())
    turtle_obj[i] = a.Turtle()
    turtle_obj[i].color(colors[i])
    turtle_obj[i].shape('turtle')
    turtle_obj[i].penup()
    turtle_obj[i].goto(-160,120-(i*40))

"""
turtle1.penup()
turtle1.goto(-160,120)

turtle2= a.Turtle()
turtle2.color('blue')
turtle2.shape('turtle')

turtle2.penup()
turtle2.goto(-160,80)


turtle3= a.Turtle()
turtle3.color('brown')
turtle3.shape('turtle')

turtle3.penup()
turtle3.goto(-160,40)


turtle4= a.Turtle()
turtle4.color('yellow')
turtle4.shape('turtle')

turtle4.penup()
turtle4.goto(-160,0)


turtle5= a.Turtle()
turtle5.color('green')
turtle5.shape('turtle')

turtle5.penup()
turtle5.goto(-160,-40)
"""
for rot in range(10):
        for t in range(no_of_turtles):
            turtle_obj[t].right(36)
"""
for i in range(1000):
    if(turtle2.xcor()<=(-140+(19*40)) and turtle3.xcor()<=(-140+(19*40)) and turtle4.xcor()<=(-140+(19*40))and
    turtle5.xcor()<=(-140+(19*40))
    and turtle1.xcor()<=(-140+(19*40))):
        turtle1.forward(randint(1, 5))
        turtle2.forward(randint(1, 5))
        turtle3.forward(randint(1, 5))
        turtle4.forward(randint(1, 5))
        turtle5.forward(randint(1, 5))

    else:
        break
"""

for i in range(1000):
    for t in range(no_of_turtles):
        if (turtle_obj[t].xcor() <= (-140 + (19 * 40))):
            turtle_obj[t].forward(randint(1,5))
        else:
            break



a.done()