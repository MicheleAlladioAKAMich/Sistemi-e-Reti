'''
Author: Michele Alladio
es: 
Correctly determine the fewest number of coins to be given to a customer such that the sum of the coins' value would equal the correct amount of change.

For example
An input of 15 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) or [5, 10]
An input of 40 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) and one quarter (25) or [5, 10, 25]
'''

moneyValues = [1, 5, 10, 25, 100]

def calculateChange(change):
    changeList = []

    while change != 0:  #fino a quando il resto da dare non equivale a 0
        position = -1   #variabile per il posizionamento nella lista delle valute
        for value in moneyValues:   #cicla le valute
            if value > change:  #se la valuta è maggiore del resto      
                changeList.append(moneyValues[position])    #viene inserita nella lista la valuta precedente
                change -= moneyValues[position] #viene decrementato il resto 
                break   #si interompe il ciclo
            else:  #se la valuta è minore del resto 
                position += 1  #incremento della posizione nella lista 
        
    return changeList[::-1] #lista delle valute al contrario



def main():
    change = int(input("Inserisci il resto: "))

    print(f"Resto: {calculateChange(change)}")

if __name__ == "__main__":
    main()
