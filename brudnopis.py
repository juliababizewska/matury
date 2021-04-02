with open("cyfry.txt") as cyfry:
    a = cyfry.read().split()

    a = list(map(int, a ))
    print(a)