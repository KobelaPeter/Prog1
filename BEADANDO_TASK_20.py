# 20. Feladat
# Írjon programot, amely egy szövegben megtalálja a leghosszabb palindrom részsztringet.
# A szövegben a szóközöket ingorálja és a kis és nagy betűket se különböztesse meg.



import string


str = input("Add meg a stringet!")
#takarító részleg

ls =[]
for i in str:
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


#polindromkereső függvény

def polindromok(str):
    lista = []

    for i in range(len(str)):
        for j in range(0,i):
            xx = str[j:i +1]

            if xx == xx[::-1]:
                lista.append(xx)
    return lista

lista = (polindromok(str))
print(lista)

#megnézi melyik a leghosszabb elem a listában
db = 0
xx = ""

for i in range(len(lista)):
    if int(len(lista[i])) > db:
        db = int(len(lista[i]))
        xx = lista[i]

print(xx)






