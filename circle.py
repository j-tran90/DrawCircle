import turtle

turtle.bgcolor ("black")
turtle.pensize (2)
turtle.speed (0)

for i in range (100):
    for colours in ["blue", "red", "green", "orange", "white"]:
        turtle.color(colours)
        turtle.circle (100)
        turtle.left (10)


turtle.hideturtle()