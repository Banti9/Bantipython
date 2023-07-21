import turtle as t
import colorsys as C
t.setup(700,700)
t.tracer(10)
t.width(4)
t.bgcolor("black")
def square(x):
    for i in range(3):
        t.fd(x)
        t.lt(90)

    t.fd(x)
for j in range(20):
    for i in range(10):
        t.color(C.hsv_to_rgb(i/10,1-j/20,1)) 
        t.rt(135)
        square(200-j*4)
        t.rt(135)
        t.circle(50,36)
    t.hideturtle()           