import turtle

def draw_square(x):
    for i in range(0,4):
        x.forward(100)
        x.right(90)

def loop_square():

    window = turtle.Screen()
    window.bgcolor("White")
    shape = turtle.Turtle()
    shape.color("blue")
    shape.speed(15)
    for i in range(0, 36):
        draw_square(shape)
        shape.right(10)
    shape.right(90)
    shape.forward(250)
    window.exitonclick()
loop_square()