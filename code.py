"""
Author: Michele Alladio
es: operazioni di enqueue e dequeue sulle code
"""

#wrapper
def dequeue(queue):
    return queue.pop(0)

def enqueue(queue, element):
    queue.append(element)

def main():
    coda = ["a", "b", "c", "d"]

    enqueue(coda, "z")
    print(coda)

    x = dequeue(coda)
    print(x)
    print(coda)

if __name__ == "__main__":
    main()