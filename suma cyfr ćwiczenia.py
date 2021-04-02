def suma_cyfr(a):
    s = 0
    while a > 0:
        s += a%10
        a//=10
    return s
from math import ceil, sqrt

def czy_pierwsza(a):
    if a < 2:
        return False
    if a%2==0 and a!=2:
        return False
    for i in range (3,ceil(sqrt(a))):
        if a % i ==0:
            return False
    return True


def dec_to_bin(a):
    s = ""
    while a > 0:
        s+=str(a%2)
        a = a//2
    return s[::-1]

def bin_to_dec(a):
    s = 0
    p = 1
    while a>0:
        s+=a%10*p
        a=a//10
        p = p*2
    return s
print(bin_to_dec(11001))

