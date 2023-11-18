# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that creates a blue gradient
import turtle

tess= turtle.Turtle()
turtle.colormode(255)

wn= turtle.Screen()

for i in range(10,251,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,0,i)
wn.exitonclick
