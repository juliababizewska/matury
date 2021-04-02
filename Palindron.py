with open("dane.txt","r") as dane:
    slowa = dane.read().split()
    for i in slowa:
        if i == i[::-1]:
            print(i)
            