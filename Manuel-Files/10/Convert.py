def ConvertirFar(faren):
    return (5/9)*(faren - 32)


celsius = ConvertirFar(float(input('Ingrese los grados\n')))
print(f'Los grados en celsius son {celsius}')
