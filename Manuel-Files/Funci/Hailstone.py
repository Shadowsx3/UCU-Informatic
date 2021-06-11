def Calcul(Numer):
    Numero = Numer.split('->')
    T = int(Numero[len(Numero) - 1])
    Nuevo = (T % 2) * (T * 3 + 1) + ((T % 2) - 1) * (-T // 2)
    Numer += f'->{Nuevo}'
    if Nuevo == 1:
        return Numer
    else:
        return Calcul(Numer)



Resultado = Calcul(input('Ingrese un numero\n'))
print(f'El resultado es :\n{Resultado}')
