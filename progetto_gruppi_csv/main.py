#!/usr/bin/env python3

import sys
import itertools

# Somma elementi matrice "mat" aventi indice riga e colonna
# diversi fra di loro e appartenenti a "sa"
#
# Input: mat: Matrice, sa: lista o insieme
# Output: somma celle
def somma_celle(mat, sa):
    totale = 0
    for row, arr in enumerate(mat):
        if row in sa:
            for col, elem in enumerate(arr):
                if (row != col) and (col in sa) and (len(mat[row][col]) > 0):
                    totale += int(mat[row][col])

    return totale

# Divide in 2 gruppi la matrice
#
# Input: matrice come lista di liste per riga
# Output: tupla con 2 elementi di cui ogni elemento è una lista di membri del gruppo (indice 0)
def split_groups(mat):
    n = len(mat)

    bestGroup1 = None
    bestGroup2 = None
    bestSum = float('-inf')
    for sa1 in itertools.combinations(range(n), n//2):
        # la partizione con la migliore media equivale a quella con la migliore somma
        sa2 = set(range(n)) - set(sa1)
        tmp_sum = somma_celle(mat, sa1) / len(sa1) + somma_celle(mat, sa2) / len(sa2)
        if (tmp_sum > bestSum):
            bestSum = tmp_sum
            bestGroup1 = sa1
            bestGroup2 = sa2

    return (set(bestGroup1), set(bestGroup2))

# Converte il file CSV in una matrice come lista di liste per riga
#
# Input: file CSV
# Output: matrice
def csv2mat(file):
    lines = file.read().splitlines()
    mat = []

    for i in lines:
        mat.append(i.split(','))

    return mat

# Converte la tupla dei gruppi in una stringa di cui ogni lettera indica l'indice del partecipante, i gruppi sono separati da uno spazio
#
# Input: tupla di liste di numeri da 0 a 25
# Output: stringa
def formatGroupsTuple(groups):
    output = ""
    for g in groups:
        for item in g:
            output += chr(ord('A') + item)
        output += " "

    return output

def main():
    if len(sys.argv) < 2:
        print("Devi specificare il file CSV")
        return

    with open(sys.argv[1]) as file:
        mat = csv2mat(file)
        for line in mat:
            if len(line) != len(mat):
                print("Matrice non quadrata")
                return

        groups = split_groups(mat)
        media = 0
        for g in groups:
            media += somma_celle(mat, g) / len(g)

        media /= len(groups)
        print(formatGroupsTuple(groups))
        print(media)

if __name__ == "__main__":
    main()
