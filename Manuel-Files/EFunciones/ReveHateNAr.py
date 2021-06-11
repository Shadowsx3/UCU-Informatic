def Revertir(numi):
    mil = numi // 1000
    cen = (numi - mil*1000) // 100
    dec = (numi - mil*1000 - cen*100) // 10
    uni = numi % 10
    rev = str(uni) + str(dec) + str(cen) + str(mil)
    return rev


while True:
    num = int(input('Ingrese un numero de cuatro digitos\n'))
    if num < 1000:
        break
    print(Revertir(num))
