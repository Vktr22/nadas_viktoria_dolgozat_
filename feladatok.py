import random

def parosBeker():
    szam:int=int(input("Kérek egy páros számot: "))
    while(szam%2!=0):
        szam=int(input("Ez nem páros! PÁROS számot kérek: "))
    return szam

def veletlenListaZartINtervallum(min, max):
    lista=[]
    i=0
    while(i<13):
        #szam:int=int(random.random()*(max-min)+min)
        lista.append(int(random.random()*(max-min)+min))   # *(max-min)+min
        i+=1
    return lista

def oszthatoeDb(lista, szam):
    osztdb:int=0
    for i in range(0, len(lista), 1):
        if (lista[i]%3==0):
            osztdb+=1
    return osztdb

def szovegbenKeres(szoveg, karakterHely):
    karakter=""
    if(len(szoveg)<karakterHely):
        print(f"Nincs {karakterHely}. karakter!")
    else:
        karakter=szoveg[karakterHely]
        print(f"A szöveg {karakterHely}. karaktere {karakter} - {karakter.upper()*3}")