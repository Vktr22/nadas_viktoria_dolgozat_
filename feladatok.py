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

def nevekSzama():
    jel:str="@"
    nevek:str=input(f"Adj meg nekem neveket. Egyszerre 1 nevet, majd üss entert.\nHa már nem szeretnél többet megadni, írd be:{jel}, majd enter: ")
    db:int=0
    while(nevek!="@"):
        db+=1
        nevek=input("Következő: ")
    return db

"""
print("5. feladat:")
tip1=feladatok.felhasznTipp()
tip2=feladatok.gepTipp()
feladatok.nyertes(tip1, tip2)
"""
def felhasznTipp():
    tip:str=input("Játszunk kő, papír, ollót!\nA tipped megadásához, írd be a 3 egyikét pontosan így\n'kő', 'papír', 'olló': ")
    while(tip!="kő" or tip!="papír" or tip!="olló"):
        tip=input("Nem jó!, kérlek 'kő', 'papír', vagy 'olló'-t írj:")
    return tip
#*(max-min)+min)
def gepTipp():
    tipSzam:int=int(random.random()*(3-1)+1)
    tip:str=""
    if(tipSzam==1):
        tip="kő"
    elif(tipSzam==2):
        tip="papír"
    else:
        tip="olló"
    return tip

def nyertesKiir(tipF, tipG):
    if(tipF=="kő"):
        if(tipG=="kő"):
            print("Döntetlen!")
        elif(tipG=="papír"):
            print("Én nyertem!")
        else:
            print("Te nyertél!")
    if(tipF=="papír"):
        if(tipG=="kő"):
            print("Te nyertél!")
        elif(tipG=="papír"):
            print("Döntetlen!")
        else:
            print("Én nyertem!")
    else:
        if(tipG=="kő"):
            print("Én nyertem!")
        elif(tipG=="papír"):
            print("Te nyertél!")
        else:
            print("Döntetlen!")