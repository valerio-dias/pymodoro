from turtle import Turtle, Screen
from relogio import Relogio
import pygame

pygame.mixer.init()
ring = pygame.mixer.Sound('god_sound.wav')
elephant = pygame.mixer.Sound('elephant_sound.wav')

t = Turtle()
t.hideturtle()
screen = Screen()


def tela(r, g, b, mensagem):
    screen.setup(width=800, height=600)
    screen.bgcolor(r/255, g/255, b/255)
    screen.title('PYmodoro')
    screen.tracer(0)
    t.clear()
    t.goto(0, 250)
    t.color('white')
    t.clear()
    t.write('PYmodoro', align='center', font=('Comic Sans MS', 30, 'normal'))
    t.goto(0, -250)
    t.color('white')
    t.write(mensagem, align='center', font=('Comic Sans MS', 15, 'normal'))

tela(188.0, 71.0, 73.0, 'Vamos começar?')

continua = 's'

relogio = Relogio()
while continua == 's':
    iniciar = screen.textinput(title="Tempo", prompt="Escolha quantos minutos (sugestão: 25/30/45/50):")
    int_ini = int(iniciar) * 60
    tela(45.0, 106.0, 79.0, 'Bom estudo')
    relogio.timer(int_ini)
    ring.play()
    relogio.update_tela()

    intervalo = screen.textinput(title="Intervalo", prompt="Escolha quantos minutos de intervalo (sugestão: 5/15/30) ou tecle qualquer tecla para encerrar:")
    int_int = int(intervalo) * 60
    relogio.update_tela()
    tela(29.0, 53.0, 87.0, 'Hora de levantar e beber uma água')

    relogio.timer(int_int)
    relogio.update_tela()
    elephant.play()

    continua = screen.textinput(title='Inicio/Continua', prompt='Tecle s para continuar os estudos')

    relogio.update_tela()

tela(0.0, 0.0, 15.0, 'Até à próxima!')

screen.exitonclick()