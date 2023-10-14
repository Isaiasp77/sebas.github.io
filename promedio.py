from random import randint
lista_numeros = [10,20,30,100,46,23,7457,646]
def promedio(numeros):
    a=0
    for num in numeros:
        a = a + num

    return a/(len(numeros))

print(promedio(lista_numeros))

aleatorio = randint(1,99)

print(aleatorio)
