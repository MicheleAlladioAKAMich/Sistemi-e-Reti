'''
Author: Michele Alladio
es: Leggere da due file diversi dati relativi al cambiamento climatico e creare degli appositi grafici 
temporali e a dispersione utilizzando la libreria matplotlib
'''

import matplotlib.pyplot as plt
import csv

def main():
    fileAnomalie = open("Temperature_Anomaly.csv", "r")
    fileEmissioni = open("CO2_emissions.csv")

    anni = []
    anomalie = []
    emissioniTotali = []
    emissioniCarburanteLiquido = []
    emissioniCemento = []
    gasFlaring = []

    dataReader1 = csv.reader(fileEmissioni, delimiter = ',')
    next(dataReader1)    #salto la prima riga del file

    for riga in dataReader1:
        if int(riga[0]) >= 1880:
            #leggo vari dati del file e li inserisco nelle apposite liste
            anni.append(int(riga[0]))
            emissioniTotali.append(int(riga[1]))
            emissioniCarburanteLiquido.append(int(riga[3]))
            emissioniCemento.append(int(riga[5]))
            gasFlaring.append(int(riga[6]))

    dataReader2 = csv.reader(fileAnomalie, delimiter = ',')
    #salto le righe del file "Inutli"
    next(dataReader2)    
    next(dataReader2)    
    next(dataReader2) 
    next(dataReader2) 
    next(dataReader2) 

    for riga in dataReader2:
        if(int(riga[0])) <= 2010:
            anomalie.append(float(riga[1])) #leggo le anomalie della temperatura e le inserisco in una lista

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)   #creo tre piani cartesiani per i diagrammi temporali
    fig.suptitle('Emissioni totali, emissioni derivanti dal carburante liquido ed emissioni derivanti dal cemento per gli anni dal 1880 al 2010')

    ax1.bar(anni, emissioniTotali, color = 'green') #grafico a barre verde
    ax1.set_xlabel('Anno')  #descrizione asse x
    ax1.set_ylabel('Emissioni\ntotali\n(10^6 ton)') #descrizione asse y

    ax2.plot(anni, emissioniCemento, 'o-y') #grafico temporale giallo con unione dei pallini
    ax2.set_xlabel('Anno')
    ax2.set_ylabel('Emissioni\ncemento\n(10^6 ton)')

    ax3.stem(anni, emissioniCarburanteLiquido)  #grafico a stelo blu
    ax3.set_xlabel('Anno')
    ax3.set_ylabel('Emissioni\ncarburante liquido\n(10^6 ton)')

    plt.tight_layout()  #distanzia i grafici
    plt.show()  #mostra i grafici
    

    fig, (ax4, ax5) = plt.subplots(2, 1)

    fig.suptitle('Quantità di gas utilizzato come combustibile e scostamento della temperatura per gli anni dal 1880 al 2010')

    ax4.scatter(anni, gasFlaring, color = 'purple') #grafico a dispersione viola
    ax4.set_xlabel('Anno')
    ax4.set_ylabel('gas utilizzato\ncome combustibile\n(10^6 ton)')

    ax5.scatter(anni, anomalie, color = 'orange')   #grafico a dispersione arancione
    ax5.set_xlabel('Anno')
    ax5.set_ylabel('Scostamento\ntemperatura\n(°C)')

    plt.tight_layout()  #distanzia i grafici
    plt.show()  #mostra i grafici

if __name__ == "__main__":
    main()