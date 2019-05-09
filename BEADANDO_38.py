# 38. Feladat
# Adott egy 40X100-as mátrix. A mátrix neve Mozi legyen. A moziban lehet előre
# foglalni férőhelyet. Pl.: egy hely foglalása:
# NRXXXXXXXXBAXXXXXX...
# .
# .
# .
# A helyfoglalásokat jelölje a foglaló monogramja. Így egy sorban maximum 20-an férnek
# el. XX jelölje a még szabad helyeket.
# Töltsük fel a mozit úgy, hogy a fogadott vendégek között a monogramjuk megadásával
# tudjunk keresni, módosítani és törölni foglalásokat.




import string
import numpy as np

mozi = np.empty((100,40),np.str)

for i in range(mozi.shape[0]):
    for j in range(mozi.shape[1]):
        mozi[i][j] = "X"


print("Mit szeretnél csinálni?, gepeld be: helyfoglalas, kereses, torles, indextorles, nevmodositas, indexkereses,  (0 = kilepes)")
inp = input()


while True:
    try:
        while inp !="0":

            if inp == "helyfoglalas":
                n = int(input("add meg hanyadik sorban szeretnel ulni: "))
                k = int(input("add meg hanyadik szeken(oszlopban) szeretnel ulni: "))
                mg = input("add meg a monogrammod: ")
                n = n-1
                k = k-1

                k = k*2

                if k >= mozi.shape[1] or k < 0 or n >= mozi.shape[0] or n < 0:
                    print("Nincs ilyen szék, kérlek adj meg egy másikat! ")
                    continue

                else:
                    for i in range(mozi.shape[0]):
                        for j in range(mozi.shape[1]):
                            if i == n and j == k:
                                if mozi[i,j] != "X" or mozi[i,j+1] != "X":
                                    print("Ez a hely már foglalat, kívánja felülírni? (y/n)" )
                                    xx = input()
                                    if xx == "y":
                                        mozi[i,j+1 ] = mg[1]
                                        mozi[i,j] = mg[0]
                                        break
                                    elif xx == "n":
                                        break
                                elif mozi[i, j] == "X" and mozi[i, j+1] == "X":
                                    mozi[i,j+1] = mg[1]
                                    mozi[i,j] = mg[0]


                    print(mozi)

            if inp == "kereses":
                mg = input("Add meg a monogrammját annak, akit keresel: ")

                def kereso(mg,mozi):
                    for i in range(mozi.shape[0]):
                        for j in range(0,mozi.shape[1],2):
                            if mozi[i,j] == mg[0] and mozi[i,j+1] == mg[1]:
                                return ("{}.sor, {}.széken ül a keresett személy".format(i+1,int((j/2)+1)))
                    return ("Ilyen ember nem foglalt helyet!")

                print(mozi)
                print(kereso(mg,mozi))

            if inp =="torles":
                mg = input("Add meg a monogrammját annak, akit ki szeretnél törölni: ")

                def torlo(mg,mozi):
                    for i in range(mozi.shape[0]):
                        for j in range(0,mozi.shape[1],2):
                            if mozi[i, j ] == mg[0] or mozi[i, j+1] == mg[1]:
                                print("Van ilyen személy a moziban, óhajtja törölni? (y/n)" )
                                xx = input()
                                if xx == "y":
                                    mozi[i , j ] = "X"
                                    mozi[i, j + 1] = "X"
                                    return mozi
                                elif xx == "n":
                                    return mozi
                    return "Nincs ilyen"

                torolt = torlo(mg,mozi)
                print(torolt)

            if inp == "indextorles":
                n = int(input("Add meg melyik sorból toroljek: "))
                k = int(input("Add meg melyik oszlopból(széket) töröljek: "))
                k = k-1
                n = n-1

                k = k*2

                def indextorlo(mg, mozi):
                    for i in range(mozi.shape[0]):
                        for j in range(mozi.shape[1]):
                            if i == n and j == k:
                                if mozi[i,j] !="X" and mozi[i,j+1] != "X":
                                    mozi[i,j] = "X"
                                    mozi[i,j+1] = "X"
                                    return(mozi)
                                else:
                                    return ("Ez a hely ures")

                kkk = indextorlo(mg,mozi)

                print(kkk)

            if inp == "indexkereses":
                n = int(input("Add meg melyik sorból keressek: "))
                k = int(input("Add meg melyik oszlopból(széket) keressek: "))
                n = n-1
                k = k-1
                k = k * 2


                ccc = mozi[n,k]+mozi[n,k+1]

                if ccc == "XX":
                    print("A hely üres")
                else:
                    print("{}.sorban, {}.széken(oszlopban): {} ül".format(n+1,int(k/2)+1,ccc))

            if inp == "nevmodositas":
                mg = input("Add meg a modositando monogrammjat: ")
                mg2 = input("Add meg hogy mire módósítsam a monogrammot")

                def nevmodosito(mg,mg2,mozi):
                    for i in range(mozi.shape[0]):
                        for j in range(0,mozi.shape[1],2):
                            if mozi[i,j] == mg[0] and mozi[i,j+1] == mg[1]:
                                mozi[i,j] = mg2[0]
                                mozi[i,j+1] = mg2[1]
                                return mozi
                    return "Nincs ilyen ember a moziban"

                vvv = nevmodosito(mg,mg2,mozi)

                print(vvv)

            print("Mit szeretnél csinálni?, gepeld be: helyfoglalas, kereses, torles, indextorles, indexkereses, nevmodositas (0 = kilepes)")
            inp = input()

        zz = mozi
        break

    except:
        print("A megadott dolog nem szám!")


for i in range(zz.shape[0]):
    ls = []
    for j in range(zz.shape[1]):
        ls.append(zz[i,j])
        asd = "".join(ls)
    print(asd)

    
print(zz)
