'''
Author: Michele Alladio
es: 
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
verify that any and all pairs are matched and nested correctly.
'''

stack = []

def verify(string):
    ok = True
    
    for letter in string:
        if letter == '(' or letter == '[' or letter == '{':
            stack.append(letter)
        elif letter == ')':
            #if stack.pop() != NULL:
            if stack.pop() != '(':
                ok = False
                break
        elif letter == ']':
            #if stack.pop() != NULL:
            if stack.pop() != '[':
                ok = False
                break
        elif letter == '}':
            #if stack.pop() != NULL:
            if stack.pop() != '{':
                ok = False
                break
    
    return ok

def main():
    string = input("inserisci una stringa con parentesi: ")

    ok = verify(string)

    if ok == True:
        print("Ordine parentesi corretto")
    else:
        print("Ordine parentesi errato")

if __name__ == "__main__":
    main()