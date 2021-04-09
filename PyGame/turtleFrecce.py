"""
Author: Michele Alladio
es: quando la turtle tocca un bordo della finestra vine resettata
"""

import turtle

AVANZAMENTO = 50    #spostamento avanti/indietro
ANGOLORETTO = 90    #per fare un angolo retto
MAX = 800   #lunghezza di un lato

mich = turtle.Turtle()
win = turtle.Screen()

win.setup(width=MAX, height=MAX)
win.title("My game")
win.bgcolor("green")

#DEFINIZIONI PER I PULSANTI PREMUTI
def avanti():
    mich.forward(AVANZAMENTO)
    print(mich.pos())   #printa la posizione della turtle
    if mich.ycor() > MAX/2 or mich.ycor() < -(MAX/2) or mich.xcor() > MAX/2 or mich.xcor() < -(MAX/2):
        mich.reset()    #se la turtle esce dalla finestra la resetta
    
def destra():
    mich.right(ANGOLORETTO)

def sinistra():
    mich.left(ANGOLORETTO)

def indietro():
    mich.backward(AVANZAMENTO)
    print(mich.pos())   #printa la posizione della turtle
    if mich.ycor() > MAX/2 or mich.ycor() < -(MAX/2) or mich.xcor() > MAX/2 or mich.xcor() < -(MAX/2):
        mich.reset()    #se la turtle esce dalla finestra la resetta

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
#RICHIAMA UNA DEFINIZIONE A SECONDA DEL TASTO PREMUTO
win.onkey(avanti, "Up")
win.onkey(indietro, "Down")
win.onkey(sinistra, "Left")
win.onkey(destra, "Right")    

win.mainloop()  #loop del main