#-------------------Juego del ahorado--------------------
# Variables
import random
abecedario = list(map(chr, range(97, 123))) #genero una lista con el alfabeto en minusculas
intentos = 6 #defino numero de intentos (6 si es el dibujo del ahorcado)
resultado = []
palabras = ['messi', 'computadora', 'perros', 'botella', 'televisor']
palabra = list(random.choice(palabras))
for i in range(0,len(palabra)):
    resultado.append('_')
print('...JUGUEMOS AL AHORCADO\n')
print(f'Intentá adivinar esta palabra de {len(palabra)} letras, ¿comenzamos?\n')

print (*resultado, sep=' ')
while intentos > 0:
    letra = input(f'\n      Tienes {intentos} intentos, ingrese una letra para adivinar o ingresá 0 para arriesgar: ')
    if letra == '0':
        resultado = list(input('\n\nArriesga ... ingrese la palabra: '))
        intentos = 0
    for cursor in range(0,len(palabra)):
        if letra == palabra[cursor]:
            resultado[cursor] = letra
    print('\n')
    print(*resultado, sep=' ')
    print('\n')
    intentos-=1
if resultado == palabra:
    print('Felicitaciones, adivinaste la palabra')
else:
    #palabra = ''.join(palabra) #convierto la lista en string para mostrarla en print
    print('AHORCADO!!!!! ... la palabra era ')
    print(*palabra, sep='')