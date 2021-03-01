from turtle import *

t = Turtle()
t.shape('turtle')
bgcolor('#000000')  # цвет фона холста
t.speed(10)
### код пишем тут

sides = 6
colors = ['green', 'red', 'blue', 'yellow', 'cyan', 'purple', 'black', 'orange']
for x in range(360):
    t.color(colors[x % len(colors)])
    t.fd(x * 3 / sides + x)
    t.lt(360/sides + 1)
    t.width(x * sides / 200)

#######
done()