from turtle import *

tina = Turtle()
tina.shape('turtle')


def square(x, y, length, color):
    tina.color(color)  # выбрать цвет
    tina.up()  # поднять перо
    tina.goto(x, y)  # перейти в (х, у)
    tina.down()  # опустить перо
    for i in range(4):  # повторить 4 раза
        tina.fd(length)  # идти вперед(length шагов)
        tina.rt(90)  # повернуть вправо на 90 градусов


square(50, -50, 100, 'green')

done()