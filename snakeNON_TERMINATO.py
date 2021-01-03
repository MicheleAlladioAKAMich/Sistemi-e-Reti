"""
Author: Michele Alladio
es: snake
"""
def main():
    #AGGIORNAMENTO SULLO STATO DEL PROGRAMMA:
    #creazione testa (snake): FATTO
    #creazione cibo: FATTO
    #creazione coda dello snake: FATTO
    #movimento della testa (snake): FATTO
    #riposizionamento random del cibo quando viene mangiato dallo snake: FATTO
    #aggiornamento della coda ogni volta che lo snake mangia: FATTO
    #morte dello snake quando sbatte contro un lato della finestra: FATTO
    #mostrare scritta di fine gioco: FATTO
    #fare in modo che la coda segua lo snake: DA FARE
    #morte dello snake quando sbatte contro la sua coda: DA FARE

    import turtle, time, random     #importo le librerie che mi servono

    AVANZAMENTO = 20    #spostamento turtle
    MAX = 650   #lunghezza di un lato

    #impostazioni per lo snake
    mich = turtle.Turtle() 
    mich.goto(0, MAX/2 - 50)
    mich.shape("square")    #è un quadrato
    mich.color("orange")   #imposta il colore dello snake (rosso)
    mich.direction = "stop"     #all'inizio la direzione dello snake è nulla
    mich.penup()    #lo snake non disegna

    coda = []   #la coda dello snake è un array

    #impostazioni per il cibo
    cibo = turtle.Turtle()
    cibo.speed(0)   #non si muove
    cibo.shape("circle")    #è un cerchio
    cibo.color("purple")    #colore del cibo: viola
    cibo.shapesize(1, 1)  #dimensioni
    cibo.penup()    #il cibo non disegna

    #impostazioni per la finestra di gioco (dimensioni, titolo e colore)
    win = turtle.Screen()
    win.setup(width=MAX, height=MAX)
    win.title("Snake by Michele Alladio")
    win.bgcolor("black")    

    delay = 0.1     #per ridurre il movimento della turtle
    punteggio = 0   #punteggio giocatore

    #DEFINIZIONI PER I PULSANTI PREMUTI (OGNI VOLTA SI CONTROLLA CHE NON SI RICHIEDA LA DIREZIONE INVERSA A QUELLA ATTUALE)
    def avanti():
        if mich.direction != "down":
            mich.direction = "up"
        
    def destra():
        if mich.direction != "left":
            mich.direction = "right"

    def sinistra():
        if mich.direction != "right":
            mich.direction = "left"

    def indietro():
        if mich.direction != "up":
            mich.direction = "down"

    def move():
        if mich.direction == "up":
            mich.sety(mich.ycor() + AVANZAMENTO)  #aggirnamento della coordinata (movimento della turtle)
    
        if mich.direction == "down":
            mich.sety(mich.ycor() - AVANZAMENTO)
    
        if mich.direction == "right":
            mich.setx(mich.xcor() + AVANZAMENTO)
    
        if mich.direction == "left":
            mich.setx(mich.xcor() - AVANZAMENTO)

    while True:
        win.update()    #aggiornamento della finestra di gioco
        move()  #movimento dello snake
        time.sleep(delay)   #riduzione del movimento della turtle

        #CAMBIO DI DIREZIONE
        win.listen()     #mette la finestra in ascolto di eventi (es: pressione tasti)
        #richiama una definizione a seconda del tato premuto
        win.onkey(avanti, "Up")
        win.onkey(indietro, "Down")
        win.onkey(sinistra, "Left")
        win.onkey(destra, "Right")    

        #CONTATTO CON IL CIBO
        if mich.distance(cibo) < 15:    
            #il cibo viene riposizionato randomicamente
            x = random.randint(-(MAX/2 - 20), MAX/2 - 20)
            y = random.randint(-(MAX/2 - 20), MAX/2 - 20)
            cibo.goto(x, y)

            #newCoda è il nuovo quadrato aggiunto al fondo della voda ogni colta che lo snake mangia
            newCoda = turtle.Turtle()
            newCoda.speed(0)    #la coda non si muove
            newCoda.shape("square")     #è un quadrato
            newCoda.color("green")   #è gialla
            newCoda.penup()  #non disegna
            coda.append(newCoda)    #aggiunge un nuovo quadrato alla fine della coda

            punteggio += 1  #incremento del punteggio
        
        #COLLISIONI
        if(mich.xcor() > MAX/2 - 10 or mich.xcor() < -(MAX/2 - 10) or mich.ycor() > MAX/2 - 20 or mich.ycor() < -(MAX/2 - 20)): #uscita dallo schermo
            #turtle che scrive il messaggio della fine del gioco e il punteggio
            pen = turtle.Turtle()
            pen.color("white")
            pen.goto(0,0)
            pen.write("HAI PERSO!!!\n Punteggio: {} ".format(punteggio), align="center", font=("Calibri", 30, "normal"))    #scritta di fine partita

            mich.color("red")   #la testa dello snake diventa rossa
            time.sleep(3)   #aspetta 3 secondi prima di chiudere la finestra
            mich.pos(0,0)   #se non riposiziono lo snake si blocca il programma
        
if __name__ == "__main__":
    main()  #richiamo il main