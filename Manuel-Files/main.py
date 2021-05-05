x = input("Ingrese los valor de los tres lados: ").split()
Triangulos=['equilatero','isoceles','escaleno']
tipo=0
x.sort()
for i in range(0,len(x)-1):
    if(x[i]!=x[i+1]):
        tipo+=1
print('El triangulo es '+Triangulos[tipo])