f = open('datos.txt', 'w')
for i in range(0, int(input('Num max\n'))):
    a = i
    b = a*3
    f.write(f'{a},{b}\n')
f.close()
