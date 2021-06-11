import random

f = open('datos.txt', 'w')
for i in range(1, int(input('Num max\n'))):
    a = random.randint(1, 9)
    b = random.randint(1, 10000)
    c = int(b % a == 0)
    f.write(f'{a},{b},{c}\n')
f.close()
