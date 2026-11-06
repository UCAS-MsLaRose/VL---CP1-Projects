#VL, Library notes
import turtle as t


t.showturtle()

#t.forward(250)
"""t.left(120)
t.forward(250)
t.left(120)
t.forward(250)
t.width(10)
t.color("purple")
t.up()
t.forward(200)
t.down()
t.forward(200)
t.home()
t.pos()
t.left(100)
t.forward(100)


t.exitonclick()
"""
"""
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
loop_helper = 0

t.showturtle()
t.speed(100)

for num in range(360):
    t.color(colors[loop_helper])
    t.fd(3)
    t.left(1)

    loop_helper += 1
    if loop_helper == 6:
        loop_helper = 0
"""
red = t.Turtle()
blue = t.Turtle()
red.color("red")
t.hideturtle()
t.forward(200)
t.showturtle()
print(t.xcor())
t.forward(200)
t.up()
t.goto(40,80)
t.shape("turtle")
red.forward(200)


t.exitonclick()