def Ejer2(nume):
    return nume ** 2 - 4


print(Ejer2(int(input('Ingrese un numero\n'))))










def Ejer4(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


def Ejer6(horas, minutos, segundos, horas2, minutos2, segundos2):
    return abs(3600*(horas-horas2) + 60*(minutos-minutos2)+(segundos-segundos2))
