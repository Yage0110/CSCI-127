# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
#Random turtle walk

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  a = random.randrange(0,360,1)
  trey.forward(10)
  trey.right(a)
