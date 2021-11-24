from datetime import timedelta
from time import sleep
from turtle import Turtle

class Relogio(Turtle):
    def __init__(self, segundos):
        super().__init__()
        self.segundos = segundos
        self.tempo = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.timer()
        self.update_tela()

    def timer(self):
        self.tempo = timedelta(seconds=self.segundos)
        while str(self.tempo) != '0:00:00':
            self.update_tela()
            self.tempo = self.tempo - timedelta(seconds=1)
            sleep(1)

    def break_time(self, segundos):
        self.tempo = timedelta(seconds=segundos)
        while str(self.tempo) != '0:00:00':
            self.update_tela()
            self.tempo = self.tempo - timedelta(seconds=1)
            sleep(1)

    def update_tela(self):
        self.clear()
        self.goto(0, 0)
        self.write(self.tempo, align="center", font=("Courier", 80, "normal"))
