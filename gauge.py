import turtle as t
import myArc as a
#r1=int(input("Enter the radius of inner circle :"))/2

#r2=int(input("Enter the radius of outer circle :"))/2

#no_of_div=int(input("Enter no. of kg pressure value:"))

r1=300
r2=350
no_of_div=7

#main_div_val=360/no_of_div
main_div_val=270/no_of_div
t.setup(width=0.99, height=0.99, startx=0, starty=0)

#Draw inner arc
t.speed(15)

t.penup()
t.right(90)  # Face South
t.forward(r1)  # Move radius
t.right(270)
t.pendown()
a.__CreateArc(45,315,r1,t)
#t.circle(r1)
t.penup()
t.home()

t.right(90)  # Face South
t.forward(r2)  # Move one radius
t.right(270)
t.pendown()
t.circle(r2)
t.penup()
t.home()

print(main_div_val)
b=[225]
# Main Division of inner Circle
t.color("red")

for i in range(no_of_div+1):
    t.left(b[i])
    t.forward(r1-7)
    t.pendown()
    t.forward(14)
    t.penup()
    t.forward(20)
    t.pendown()
    if i==0:
        t.write(0)
    else:
        t.write(b[i])
    t.penup()
    t.home()
    #b.append(main_div_val*(i+1))
    b.append(225-(main_div_val * (i + 1)))
    print(i,":",b[i])


no_of_sub_div=4
diff=b[0]-b[1]
new_diff=diff/4


#Sub-Division of Inner Circle

for j in range(len(b)-2):
    for i in range(no_of_sub_div):
        t.left(b[j] - ((i + 1) * new_diff))
        t.forward(r1-3)
        t.pendown()
        t.forward(6)
        t.penup()
        t.home()



ts=t.getscreen()
ts.getcanvas().postscript(file="test3.eps")
t.done()


