import turtle
import time

#cuadro
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
   


turtle.penup()
turtle.setx(-40)
turtle.sety(0)
turtle.pendown()

#triangulo
turtle.right(180)
turtle.forward(90)
turtle.right(135)
turtle.forward(77)
turtle.right(100)
turtle.forward(68)

turtle.penup()
turtle.setx(170)
turtle.sety(0)
turtle.pendown()
turtle.right(185)
#hexagono
for _ in range(6):
    turtle.forward(50)
    turtle.right(60)

time.sleep(1)
