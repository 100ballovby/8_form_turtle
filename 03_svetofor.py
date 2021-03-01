from turtle import *

t = Turtle()
t.shape('turtle')
t.speed(10)
### код пишем тут
t.fillcolor('gray')
t.begin_fill()
for line in range(2):
    t.fd(250)
    t.rt(90)
    t.fd(500)
    t.rt(90)
t.end_fill()

min = int(input('Сколько минут прошло? '))

if min % 2 == 0:
    t.color('red')
    t.up()
    t.goto(125, -150)
    t.down()
    t.circle(50)
else:
    t.color('green')



#######
done()