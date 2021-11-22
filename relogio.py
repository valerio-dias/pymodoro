from datetime import datetime, timedelta
from sys import stdout
from time import sleep
from turtle import Turtle


class Relogio(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.time_screen = 25
        self.timer()
        self.update_tela()
   
    def timer(self):
        self.segundos = 1500
        self.tempo = timedelta(seconds=self.segundos)
        while self.tempo !=  '0:00:00':
            sleep(1)
            self.update_tela()
            self.tempo = self.tempo - timedelta(seconds=1)
            # self.update_tela()

    def update_tela(self):
        self.clear()
        self.goto(0, 0)
        self.write(self.tempo, align="center", font=("Courier", 80, "normal"))
     