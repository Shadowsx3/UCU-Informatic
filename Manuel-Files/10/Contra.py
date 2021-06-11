import random
import hashlib
contra = ''
ter = int(input('De cuantos caracteres debe ser la contraseña?\n'))
while ter > 0:
    contra += str(random.randint(0, 9))
    ter -= 1
print(f'La contraseña es: {contra}')




"""for i in range(0, int(input('De cuantos caracteres debe ser la contraseña?\n'))):
    contra += str(random.randint(0, 9))
print(f'La contraseña es: {contra}')
h = hashlib.new('sha512_256')
h.update(b"{contra}")
print(f'La contraseña real es: {h.hexdigest()}')"""
