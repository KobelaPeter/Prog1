# 20. Feladat
# Írjon programot, amely egy szövegben megtalálja a leghosszabb palindrom részsztringet.
# A szövegben a szóközöket ingorálja és a kis és nagy betűket se különböztesse meg.



import string


str1 = input("Add meg a stringet!")


ls =[]
for i in str1:
    if i in string.punctuation:
        continue
    elif i == " ":
        continue
    else:
        ls.append(i)

str = "".join(ls)


lista = []

for i in range(len(str)):
    for j in range(0,i):
        szo = str[j:i+1]
        szo2 = szo[::-1]

        if szo.capitalize() == szo2.capitalize():
            lista.append(szo)

#print(lista)


xx = ''
db = 0

for i in range(len(lista)):
    if int(len(lista[i])) > db:
        db = int(len(lista[i]))
        xx = lista[i]

print(xx)
