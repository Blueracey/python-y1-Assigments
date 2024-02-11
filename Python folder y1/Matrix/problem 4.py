input1 = str(input("imput a number "))
base1 = int(input("imput it's base between 2 and 16 "))
if base1>16 and base1<2: # checks to make sure the first input is valid 
    print("sorry that is an invalid entry try again")
    base1 = int(input("imput it's base between 2 and 16 "))
    if base1>16 and base1<2:    #checks the second chance input 
            print("nice try, ending program")
            exit
base2 = int(input("imput the base you want to convert to"))
if base2>16 and base2<2:
    print("sorry that is an invalid entry try again")
    base1 = int(input("imput it's base between 2 and 16 "))
    if base2>16 and base2<2:
            print("nice try, ending program")
            exit


def convert():
    Number = int(input1,base1)


    result = ' '
    while Number > 0:
        remainder = Number % base2
        result = '012345678910ABCDEF'[remainder] + result
        Number //= base2
    print(result)



convert()


# 8723782367 base 9 = 14c88a65b in base 15 
#  123456789ABCDEF1 base 16 = 1311768467463790321 base 10
# 11111110111011011011111011101111 base 2 = DCCB0CCD base 16