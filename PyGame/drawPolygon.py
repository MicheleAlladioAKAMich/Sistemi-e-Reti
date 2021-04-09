#Author: Michele Alladio
#es: tramite il modulo turtle disegna un poligono regolare con n lati inseriti in input

"""
from turtle import *    #importa tutte le classi presenti nel modulo turtle
num = (int) (input("Inserisci un numero: "))

color('blue', 'yellow')
begin_fill()

for k in range (num):
    forward(100)
    left(360 / num)
"""

import turtle         #importa il modulo turtle
mich = turtle.Turtle()

mich.color("red")
mich.begin_fill()
nLati = (int) (input("Inserisci il numero di lati: "))
for k in range (nLati):
    mich.forward(50)
    mich.left(360 / nLati)

mich.end_fill()

