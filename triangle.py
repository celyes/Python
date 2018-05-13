import turtle
def draw_sq(x):
    for i in range(0,3):
        x.forward(100)
        x.right(-120)
def draw_triangle():

    window = turtle.Screen()
    window.bgcolor("blue")
    shape = turtle.Turtle()
    shape.color('black')
    shape.speed('25')
    for i in range (0, 36):
        draw_sq(shape)
        shape.right(10)
    window.exitonclick()
draw_triangle()
