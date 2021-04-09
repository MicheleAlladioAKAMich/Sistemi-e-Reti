#Author: Michele Alladio

vet = [9,7,8,5,6,3,4,1,2,0]

def selectionSort(v):
    n = len(vet)
    for k in range (n-1):
        kmin = k
        for j in range (k+1, n):
            if(v[kmin] > v[j]):
                kmin = j
        if(kmin != k):
            v[k], v[kmin] = v[kmin], v[k]

print(vet)
selectionSort(vet)  #ordinamento del vettore
print(vet)