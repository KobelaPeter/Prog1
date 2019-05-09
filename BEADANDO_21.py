# 21. Feladat
# A 2520 a legkisebb szám ami maradék nélkül osztható minden számmal 1 és 10 között.
# Írjon programot, amely meghatározza a legkisebb számot ami osztható 1 és N között
# lévő összes számmal. Az implementáció legyen ötletes és hatékony, közel valós időben
# fusson le akár N=20-ra is.

import time
import numpy as np

n = int(input("Adj meg egy szamot: "))
ls = np.arange(1,n+1)

#t = time.process_time()

if n == 0:
    print(0)

if n%2 == 0:
    a = n//2
else:
    a = n//2+1

lista = ls[-a:]
print(lista)
q = 0
i = 0
while True:
    z = 0
    for j in lista:
        if i % j != 0:
            break
        else:
            z +=1
    if z == len(lista):
        q = i
        if q != 0:
            break
    i += n

print(q)
#eltelt_ido = time.process_time() - t
#print("futasi ido:" ,eltelt_ido, "mp")
