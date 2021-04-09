file = open("Volo_drone.csv", "r")  #apertura file
for riga in file:
    print(riga, end = " ")  #la end mette uno spazio al posto della messa a capo inserita dalla print

file.close()    #chisura file
file = open("Volo_drone.csv", "r")  #apertura file    

for riga in file:
    print(riga[:-1].split(","))  #si ottine una lista senza il \n al fondo
file.close()    #chisura file