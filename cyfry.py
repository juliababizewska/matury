def sumacyfr(a):
    suma = 0
    while a!=0:
        suma+=a%10
        a//=10
    return suma
lista=[]
def podpunktA():
    with open("cyfry.txt", "r") as cyfry:
        liczba = cyfry.read().split()
        parzyste = 0
        f = open("zadanie4.txt", "w")
        for i in liczba:
            if int(i) % 2 == 0:
                parzyste += 1
        f.write(f"{parzyste}")

def podpunktB():
with open("cyfry.txt", "r") as cyfry:
    liczba = cyfry.read().split()
    for i in liczba:
        lista.append(sumacyfr(int(i)))
    print(max(lista))
    print(min(lista))

with open("cyfry.txt", "r") as cyfry
    liczba = cyfry.read().split()
    for i in liczba:
        while len(i)!=0:
            if i[1]<i[2]


