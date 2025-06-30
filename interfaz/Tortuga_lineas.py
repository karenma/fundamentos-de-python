import turtle
import time

lapiz1=turtle.Turtle()
lapiz2=turtle.Turtle()


lapiz1.color("red")
lapiz2.color("blue")
#posicionar lapiz 1
lapiz1.penup()
lapiz1.setx(-200)
lapiz1.sety(80)
lapiz1.pendown()

#posicionar lapiz 2
lapiz2.penup()
lapiz2.setx(-200)
lapiz2.sety(40)
lapiz2.pendown()

#dibujo del lapiz 1
for _ in range(15):
    lapiz1.penup()
    lapiz1.forward(5)
    lapiz1.pendown()
    lapiz1.forward(20)

#dibujo del lapiz 2
for i in range (20):
    lapiz2.penup()
    lapiz2.forward(7)
    lapiz2.pendown()
    lapiz2.forward(7 + i)

turtle.done()