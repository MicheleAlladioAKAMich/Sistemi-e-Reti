import sys
import serial, time
import pygame as pg
import threading, queue
import time


#pygame config
width = 1200
height = 800
screen = pg.display.set_mode((width, height))   #settaggio dello schermo
clock = pg.time.Clock()     #per gestire le tempistiche
ball = pg.image.load("/home/samuele/Scaricati/intro_ball.gif")  #immagin
ballrect = ball.get_rect() 
#coordinate della palla
ballrect.centerx = width//2
ballrect.centery = height//2

#colore
black = 0, 0, 0
dt = 1
gamma = 0.05
q = queue.Queue()

class Read_Microbit(threading.Thread):
    def init(self):
        threading.Thread.init(self)
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        #serial config
        port = "/dev/tty0"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)


running = True
rm = Read_Microbit() #legge i dati da microbit
rm.start()
pg.init()
speed = [0, 0]
while running:
    acc = q.get()
    speed[0] = (1.-gamma)speed[0] + dtacc[0]/1024.
    speed[1] = (1.-gamma)speed[1] + dtacc[1]/1024.
    q.task_done()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pg.display.flip()
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

rm.terminate()
rm.join()