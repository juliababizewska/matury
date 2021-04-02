def bin_to_dec(a):
    s = 0
    p = 1
    a = int(a)
    while a > 0:
        s += a % 10 * p
        a = a // 10
        p = p * 2
    return s


def podpunktA():
    with open("binarne.txt") as binarne:
            a = binarne.read().split()
            liczbadwucyklicznych = 0
            dwucykliczne = []
            maks = 0
            nmaks = ""
            for i in a:
                d = int(len(i)/2)
                if i[:d]== i[d:]:
                    liczbadwucyklicznych+=1
                    dwucykliczne.append(i)
                    if len(i) > maks:
                        maks = len(i)
                        nmaks = i
            '''dlugosc = []
            for i in dwucykliczne:
                dlugosc.append(len(i))'''
            print(liczbadwucyklicznych)
            print(maks)
            '''indeks = dlugosc.index(max(dlugosc))
            print(dwucykliczne[indeks])'''
            print(nmaks)
def podpunktB():
    with open("binarne.txt") as binarne:

        a = binarne.read().split()
        ilosc = 0
        dlugosc = 100
        for i in a:
            for x in range(0, len(i) - 3, 4):
                if bin_to_dec(int(i[x:x+4]))>9:
                    ilosc+=1
                    if dlugosc > len(i):
                        dlugosc = len(i)
                    break
        print(ilosc)
        print(dlugosc)

with open("binarne.txt") as binarne:
    a = binarne.read().split()
    a = list(map(bin_to_dec,a))
    najwd = 0
    najwb = ""
    for i in a:
        if i<65535:
            if i>najwd:
                najwd = i
                najwb =bin(i)
    print(najwb," ",najwd)

