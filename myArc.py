
def __CreateArc(in_angle, finish_angle, radius, tur):
    tur.penup()

    for i in range(in_angle):
        tur.circle(radius, 1)
    tur.pendown()
    for _ in range(in_angle, finish_angle):
        tur.circle(radius, 1)



import airtravel as a

a_obj=a.Flight("AIRID745")
print(a_obj.number())


