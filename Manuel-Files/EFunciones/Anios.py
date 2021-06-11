def edad(edad_num, nombre):
    tipo = 'mayor'
    if edad_num < 18:
        tipo = 'menor'
    print(f"{nombre}, eres {tipo} de edad")
