def podpunkt41():
    with open("liczby.txt", "r") as liczby:
        suma = 0
        for i in liczby:
            jedynki = i.strip().count("1")
            zera = i.strip().count("0")
            if zera > jedynki:
                suma += 1
        print(suma)
    with open("wynik4.1", "w") as wynik:
        wynik.write(f'{suma}')
def bin_to_dec(a):
    p = 1
    s = 0
    for i in range(len(a)-1,-1,-1):
        s+=int(a[i])*p
        p*=2
    return s

def podpunkt42():
    with open("liczby.txt", "r") as liczby:
        dzielne2 = 0
        dzielne8 = 0
        for i in liczby:
            if bin_to_dec(i.strip())%2==0:
                dzielne2+=1
            if bin_to_dec(i.strip())%8==0:
                dzielne8+=1
        print(dzielne2,dzielne8)

with open("liczby.txt","r") as liczby:

    print(liczby)
    max = 0
    wiersz = 1
    maxwiersz = 0
    min = 10000
    minwiersz = 0
    for y in liczby:
        if max < bin_to_dec(y.strip()):
            max = bin_to_dec(y.strip())
            maxwiersz = wiersz

        if min > bin_to_dec(y.strip()):
            min = bin_to_dec(y.strip())
            minwiersz = wiersz
        wiersz += 1
    print(minwiersz)
    print(maxwiersz)







