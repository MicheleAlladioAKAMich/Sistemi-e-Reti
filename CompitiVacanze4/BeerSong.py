'''
Author: Michele Alladio
es: 
Recite the beer song
'''

def main():
    for i in range(1,100):
        print(f"{100-i} bottles of beer on the wall, {100-i} bottles of beer. Take one down and pass it around, {99-i} bottles of beer on the wall.")

    print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
    
if __name__ == "__main__":
    main()