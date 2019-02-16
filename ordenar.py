#!/usr/bin/python3

def grande(letra):
    return letra.upper()

letras = ['a', 'Z', 'b', 'c', 'A']
ordenadas = sorted(letras, key=lambda i : i.upper())

for l in ordenadas:
    print(l)
