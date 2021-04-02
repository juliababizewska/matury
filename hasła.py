with open("hasla.txt", "r") as hasla:
    haslo = hasla.read().split()
    def podpunktA():
        parzyste = 0
        nieparzyste = 0
        f = open("wynik4a.txt.", "w")
        for i in haslo:
            if len(i) % 2 != 0:
                nieparzyste += 1
            else:
                parzyste += 1
        f.write(f"{str(parzyste)} ")
        f.write(f"{str(nieparzyste)} ")
    def podpunktB():
        f = open("wynik4b.txt", "w")
        for i in haslo:
            if i == i[::-1]:
                f.write(f"{i}\n")
    def podpunktC():
       f = open("wynik4c.txt", "w")
       for i in haslo:
           sumaliter = len(i)
           for x in range(len(i) - 1):
               if ord(i[x]) + ord(i[x + 1]) == 220:
                   f.write(f"{i}\n")
                   break
podpunktA()
podpunktB()
podpunktC()