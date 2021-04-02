def czy_pierwsza(a):
    for i in range(2,a,2):
        if a%i==0:
            return 0
        else:
            return 1
with open("NAPIS.TXT") as napis:
    napis = napis.read().split()
    napispierwszy = 0
    for i in napis:
        suma = 0
        for a in i:
            suma+=int(ord(a))
        if czy_pierwsza(int(suma))==0:
            napispierwszy+=0
        else:
            napispierwszy+=1
    print(napispierwszy)