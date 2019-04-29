# 20. Feladat
# Írjon programot, amely egy szövegben megtalálja a leghosszabb palindrom részsztringet.
# A szövegben a szóközöket ingorálja és a kis és nagy betűket se különböztesse meg.


#palindrom:
#(a szűkebb, eredeti értelemben) olyan szó vagy szókapcsolat, amely visszafelé olvasva is ugyanaz.
#egy betűt nem tekintek palindromnak


import string


str1 = input("Add meg a stringet!")

#takarító részleg

ls =[]
for i in str1:
    if i.islower():
        ls.append(i)
    elif i.isupper():
        u = i.lower()
        ls.append(u)
    elif i in string.punctuation:
        continue
    elif i == " ":
        continue
    else:
        ls.append(i)

str = "".join(ls)


#palindromkereső


lista = []

for i in range(len(str)):
    for j in range(0,i):
        szo = str[j:i+1]
        szo2 = szo[::-1]

        if szo == szo2:
            lista.append(szo)

#print(lista)

#megnézi melyik a leghosszabb elem a listában

xx = ''
db = 0

for i in range(len(lista)):
    if int(len(lista[i])) > db:
        db = int(len(lista[i]))
        xx = lista[i]

print(xx)







