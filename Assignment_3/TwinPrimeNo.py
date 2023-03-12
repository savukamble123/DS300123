def PrimeNo(a):
    if a<2:
        return False
    for i in range (2,a):
        if a % i == 0:
            return False
    return True

def TwinNo(b):
    for i in range(b + 1):
        j = i + 2
        if (PrimeNo(i) and PrimeNo(j)):
            print("{0} and {1}".format(i,j))
TwinNo(20)