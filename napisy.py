def podpunktA():
    with open("napisy.txt") as napisy:
        slowa=napisy.read().split()
        parzyste=0
        for i in slowa:
            if len(i)%2==0:
                parzyste+=1
        f = open("zadanie42013.txt","w")
        f.write(f"{parzyste}")
def podpunktB():
    with open("napisy.txt") as napisy:
        slowa = napisy.read().split()
        ilosc = 0
        for i in slowa:
            if i.count("0")==i.count("1"):
                ilosc+=1
        f = open("zadanie42013.txt", "w")
        f.write(f"{ilosc}")
def podpunktC():
    with open("napisy.txt") as napisy:
        slowa = napisy.read().split()
        zera = 0
        jedynki = 0
        for i in slowa:
            if i.count("0")==len(i):
                zera += 1
            if i.count("1")==len(i):
                jedynki += 1
        f = open("zadanie42013.txt", "w")
        f.write(f"samych zer:{zera} samych jedynek:{jedynki}")

podpunktC()
def podpunktD()
    with open("napisy.txt") as napisy:
        slowa= napisy.read().split()
        lista =[0]*17
        for i in slowa:
            dlugosc = len(i)
            lista[dlugosc]+=1
    f = open("zadanie42013.txt", "w")
    f.write(f"{lista}")