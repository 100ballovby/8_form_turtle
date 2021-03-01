from turtle import *

t = Turtle()
t.shape('turtle')
### код пишем тут
t.speed(10)
'''for x in range(10):
    t.fd(x + 5)
    t.lt(500)
'''
import random
colors = ['green', 'red', 'blue', 'yellow', 'cyan', 'purple', 'black']

for line in range(360):
    # t.color(random.choice(colors))
    t.color(colors[line % 7])
    t.fd(100)
    t.fd(-100)
    t.rt(1)


#######
done()