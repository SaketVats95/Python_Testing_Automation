"""f=open("D:\\SharedFolder\\example.com\\App_Data\\uploads\\Saket_CV.docx","r",encoding="ISO-8859-1")


b=str(f.readline()).split("\\")
for i in range(len(b)):
    print(b[i])
"""

import turtle as t

t.setup(width=0.99, height=0.99, startx=100, starty=100)

#t.setup(800,1200,0,0)
print(t.Screen().screensize())
print(t.window_height())
t.circle(150)

ts = t.getscreen()

print(ts)
ts.getcanvas().postscript(file="duck.eps")

t.done()



