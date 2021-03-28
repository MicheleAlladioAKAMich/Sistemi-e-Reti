'''
Author: Michele Alladio
es: creazione di 4 grafici basati sul file csv (dati personali)
'''

import matplotlib.pyplot as plt
import csv

def main():
    file = open("mesi.csv", "r")
    mese = []
    temperaturaMedia = []
    giorniGiacca = []
    giorniScuola = []
    giorniVideogiochi = []

    dataReader = csv.reader(file, delimiter = ',')
    next(dataReader)    #salto la prima riga del file

    for riga in dataReader:
        #lettura ed inserimento dei dati nelle aposite liste
        mese.append(riga[0])
        temperaturaMedia.append(float(riga[1]))
        giorniGiacca.append(int(riga[2]))
        giorniScuola.append(int(riga[3]))
        giorniVideogiochi.append(int(riga[4]))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    fig.suptitle('Media dei gradi per ogni mese, stima dei giorni di uso della giacca per ogni mese,\nstima dei giorni di scuola per ogni mese, stima dei giorni di uso dei videogiochi per ogni mese')

    #creazione dei grafici
    ax1.plot(mese, temperaturaMedia, 'o-g') # o: crea un punto ad ogni dato   -: collega i punti    g: green, colore verde
    ax1.set_xlabel('Mese')
    ax1.set_ylabel('Temperatura\nmedia (°C)')

    ax2.plot(mese, giorniGiacca, 'o-r')
    ax2.set_xlabel('Mese')
    ax2.set_ylabel('Giorni di uso\ndella giacca')

    ax3.plot(mese, giorniScuola, 'o-y')
    ax3.set_xlabel('Mese')
    ax3.set_ylabel('Giorni\ndi scuola')

    ax4.plot(mese, giorniVideogiochi, 'o-b')
    ax4.set_xlabel('Mese')
    ax4.set_ylabel('Giorni di uso\ndei videogiochi')

    plt.tight_layout()  #distanzia i grafici
    plt.show()  #mostra i grafici



if __name__ == "__main__":
    main()