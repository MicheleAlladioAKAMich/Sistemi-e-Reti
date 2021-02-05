"""
Author: Michele Alladio
es: operazioni di push e pop sulle pile
"""

def push_(stack, element):
    stack.append(element)

def pop_(stack):
    return stack.pop()

def main():
    pila = ["a", "b", "c", "d"]
    stringa = 'ciao'

    push_(pila, "z")
    print(pila)
    x = pop_(pila)
    print(x)
    print(pila)

if __name__ == "__main__":
    main()