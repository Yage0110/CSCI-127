# Jay Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Program that prints a turning turtle

import turtle
jasp = turtle.Turtle()

nums = []

for i in range(5):
    num = int(input("Enter a number:"))
    nums.append(num)
for num in nums:
    jasp.left(num)
    jasp.forward(100)
