a = 9048
b = 182
def GCD (a ,b ):
    if (b == 0 ):
        print(a)
    else :
        r = a % b
        return GCD (b , r)
GCD(9048,182)