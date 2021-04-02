def podpunkt1():
    with open("slowa.txt") as slowa:
        slowa = slowa.read().split()
        lista = [0]*13
        for i in slowa:
            dlugosc = len(i)
            lista[dlugosc]+=1
            f = open("wynik5.txt", "w")
        for i in range(1,len(lista)):
            print(i,lista[i])
            f.write(f"{i} : {lista[i]}\n")

with open ("slowa.txt") as slowa:
    slowa = slowa.read().split()
    with open("nowe.txt") as nowe:
        nowe = nowe.read().split()
print(slowa)
print(nowe)
for i in range (len(nowe)):
    print(nowe[i], slowa.count(nowe[i]), slowa.count(nowe[i][::-1])  )
