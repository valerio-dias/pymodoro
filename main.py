from turtle import Turtle, Screen
from relogio import Relogio
import pygame

pygame.mixer.init()
ring = pygame.mixer.Sound('god_sound.wav')
elephant = pygame.mixer.Sound('elephant_sound.wav')

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

continua = 's'

relogio = Relogio()
while continua == 's':
    iniciar = screen.textinput(title="Tempo", prompt="Escolha quantos minutos (sugestão: 25/30/45/50):")
    int_ini = int(iniciar) * 60
    t.clear()
    t.goto(0, 250)
    t.color('white')
    t.clear()
    t.write('PYmodoro', align='center', font=('Comic Sans MS', 30, 'normal'))
    t.goto(0, -250)
    t.color('white')
    t.write('Bom estudo.', align='center', font=('Comic Sans MS', 15, 'normal'))
    screen.bgcolor(188.0 / 255, 71.0 / 255, 73.0 / 255)
    relogio.timer(int_ini)
    ring.play()
    relogio.update_tela()

    intervalo = screen.textinput(title="Intervalo", prompt="Escolha quantos minutos de intervalo (sugestão: 5/15/30) ou tecle qualquer tecla para encerrar:")
    int_int = int(intervalo) * 60
    relogio.update_tela()
    t.clear()
    t.goto(0, 250)
    t.color('white')
    t.clear()
    t.write('PYmodoro', align='center', font=('Comic Sans MS', 30, 'normal'))
    t.goto(0, -250)
    t.color('white')
    t.write('Hora de levantar e beber uma água.', align='center', font=('Comic Sans MS', 15, 'normal'))
    screen.bgcolor(29.0 / 255, 53.0 / 255, 87.0 / 255)
    relogio.timer(int_int)
    relogio.update_tela()
    elephant.play()


    continua = screen.textinput(title='Inicio/Continua', prompt='Tecle s para continuar os estudos')

    relogio.update_tela()

t.clear()
t.goto(0, 250)
t.color('white')
t.clear()
t.write('PYmodoro', align='center', font=('Comic Sans MS', 30, 'normal'))
t.goto(0, -250)
t.color('white')
t.write('See u later!!!', align='center', font=('Comic Sans MS', 15, 'normal'))
screen.bgcolor(0.0 / 255, 0.0 / 255, 15.0 / 255)

screen.exitonclick()