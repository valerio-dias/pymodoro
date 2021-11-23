from turtle import Turtle, Screen
import datetime
from relogio import Relogio
import pygame

pygame.mixer.init()
ring = pygame.mixer.Sound('god_sound.wav')
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
t.goto(0, -250)
t.color('white')
t.write('Bom estudo.', align='center', font=('Comic Sans MS', 15, 'normal'))

iniciar = screen.textinput(title="Início", prompt="Escolha quantos minutos (25/30/45/57:")

int_ini = int(iniciar) * 60
relogio = Relogio(int_ini)
ring.play()

screen.exitonclick()