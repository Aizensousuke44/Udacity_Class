import turtle

from turtle import *

def draw_star():
    star = turtle.Turtle()
    star.color('red', 'blue') # first is color of line, later is underground
    star.speed(5)
    star.begin_fill()
    while True:
        star.forward(200)
        star.left(170)
        if abs(star.pos()) < 1:
            break
    star.end_fill()
    done()

def draw_circle():
    _circle = turtle.Turtle()
    _circle.color('grey')
    _circle.begin_fill()
    _circle.circle(200)
    _circle.end_fill()
    done()

def draw_square(_turtle):
    for i in range(4):
        _turtle.forward(100)
        _turtle.left(90)

def draw_():
    square = turtle.Turtle()
    square.color('red', 'black')
    square.speed(10)
    square.begin_fill()

    for i in range(36):
        draw_square(square)
        square.right(10)
    square.end_fill()
    turtle.done()

if __name__ == '__main__':
    # draw_square()
    # draw_circle()
    draw_()

