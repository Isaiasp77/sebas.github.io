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
palabra_oculta = ['_']*len(palabra)
intentos = 6
correctas = []
incorrectas = []
 
print(f'Juego del Ahoraco debe adivinar la palabra con {len(palabra)} letras')
print(palabra_oculta)

while intentos > 0:
    letra_ingresada= input(f"ingrese una letra para adivinar la plabra tienes {intentos} o ingrese 1 para adivinar la palabra:\n")
    if letra_ingresada == '1':
         palabra_oculta = list(input('Arriesga la palabra:\n'))
    ind = 0
    for letra in palabra:
        if letra == letra_ingresada:
            palabra_oculta[ind] = letra_ingresada
            correctas.append(letra_ingresada)
        ind +=1   
    else:
        incorrectas.append(letra_ingresada)
    intentos -=1
    print(palabra_oculta)
if palabra_oculta == palabra:
        intentos -= 5
        print(f'Ganaste la palabra es {palabra_oculta}')
        
else:
        print(f'Perdiste la palabra es {palabra}')