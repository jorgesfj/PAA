from functools import total_ordering
from bisect import bisect_left
from heapq import merge
import time 
import csv
start = time.time()
arquivo = open('1000orddecres.csv')
linhas = csv.reader(arquivo)
lista = []
for linha in linhas:
    for i in range(len(linha)):
            lista.append(int(linha[i]))

start = time.time()
@total_ordering
class Pile(list):
    def __lt__(self, other): return self[-1] < other[-1]
    def __eq__(self, other): return self[-1] == other[-1]
 
def patience_sort(n):
    piles = []
    # sort into piles
    for x in n:
        new_pile = Pile([x])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)
 
    # use a heap-based merge to merge piles efficiently
    n[:] = merge(*[reversed(pile) for pile in piles])
 
if __name__ == "__main__":
    patience_sort(lista)
    print lista
print("--- %s seconds ---" % (time.time() - start))