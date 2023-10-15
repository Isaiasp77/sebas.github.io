#El juego debe tener una lista de palabras predefinidas de las cuales se
#elige una palabra aleatoriamente para que el jugador adivine.
#El jugador tiene un número limitado de intentos para adivinar la palabra
#(por ejemplo, 6 intentos).
#Debe mostrar las letras adivinadas y las letras incorrectas.
#El juego debe verificar si la letra ingresada por el jugador está en la
#palabra secreta y actualizar el estado del juego en consecuencia.
#El juego debe terminar cuando el jugador adivine la palabra o se quede
#sin intentos.
#Debe mostrar un mensaje de victoria o derrota al final del juego.
#Opcional: debe mostrar una representación gráfica del estado actual del
#ahorcado. Puedes usar arte ASCII para esto.
import random
palabras = ["messi","auto","boca","piso","celular"]
palabra = list(random.choice(palabras))#elejimos la palabra
palabra_oculta = ['?']*len(palabra)
intentos = 6
correctas = []
incorrectas = []
 
print(f'Juego del Ahoraco debe adivinar la palabra con {len(palabra)} letras')
print(palabra_oculta)

while intentos > 0:
    letra_ingresada= input(f"ingrese una letra para adivinar la plabra tienes {intentos} o ingrese 1 para adivinar la palabra:\n")
    if letra_ingresada == '1':
         palabra_oculta = list(input('Arriesga la palabra:\n'))
         intentos = 0
    ind = 0
    existe_letra = False
    for letra in palabra:
        if letra == letra_ingresada:
            existe_letra = True
            palabra_oculta[ind] = letra_ingresada
        ind +=1
        cont = 0
    if  existe_letra:
              correctas.append(letra_ingresada)
              if palabra_oculta== palabra:
                     intentos =0
    else:
              cont +=1
              incorrectas.append(letra_ingresada)
              intentos -=1
    if intentos == 5:
                     print("""
                            ------
                            0    |
                                 |
                                 |
                           ------------
                           """)
                     
    elif intentos == 4:
                     print("""
                            ------
                            0    |
                            |    |
                                 |
                           ------------
                           """)
    elif intentos == 3:
                     print("""
                            ------
                            0    |
                            | \  |
                                 |
                           ------------
                           """)
    elif intentos == 2:
                     print("""
                            ------  
                            0    |
                          / | \  |
                                 |
                           ------------
                     """)
    elif intentos == 1:
                     print("""
                            ------  
                            0    |
                          / | \  |
                           /     |
                           ------------
                           """)
    elif intentos == 0 :
                     print("""
                            ------  
                            0    |
                          / | \  |
                           / \   |
                           ------------
                     """)

    print(palabra_oculta)
if palabra_oculta == palabra:
        print(f'Ganaste la palabra es {palabra_oculta}')
        print(f'letras correctas ingresadas: {correctas}')
        print(f'letas incorrectas ingresadas: {incorrectas}')
        
else:
        print(f'Perdiste la palabra es {palabra}')
        print(f'letras correctas ingresadas: {correctas}')
        print(f'letas incorrectas ingresadas: {incorrectas}')
