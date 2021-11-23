from turtle import Turtle, Screen
import datetime
from relogio import Relogio

t = Turtle()
t.hideturtle()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(188.0/255, 71.0/255, 73.0/255)
screen.title('PYmodoro')
screen.tracer(0)


t.clear()
t.goto(0, 250)
t.color('white')
t.clear()
t.write('PYmodoro', align='center', font=('Comic Sans MS', 30, 'normal'))

relogio = Relogio()
relogio




screen.exitonclick()