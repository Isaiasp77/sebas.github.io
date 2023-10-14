
# numero 1
''' 
num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))

def suma(num1,num2):
    resul1 = num1 + num2
    return resul1

print("el resultado es ",suma(num1,num2))
'''
# numero 2
'''
nombre = str(input("ingrese el nombre\n"))

def saludo(nombre):
    print(f'Hola  {nombre}')

saludo(nombre)
'''
# numero 3
'''
caadena = "Esta cadena de prueba"

def invertirCadena(caadena):
    return caadena[::-1]

print(caadena[::-1])
'''

# numero 4
'''
numero = int(input("ingrese un numero para saber si es capicua\n"))

def capicua(numero):
    if(str(numero) == str(numero)[::-1]):
        return "es capicua"
    else
print(capicua(numero))
'''

# numero 5
'''
num = int(input("primer numero\n"))
num1 = int(input("segundo numero\n"))


def esDivisible(num,num1):
    if(num % num1 == 0 ):
        return " es divisible"
    else:
        return "no es divisible"
    
print(esDivisible(num,num1))
'''

#numero 6 
'''
numero = int(input("ingrese numero para saber si es par\n"))

def es_par(numero):
    if(numero % 2 == 0):
        return "es par"
    else:
        return " es impar"
    
print(es_par(numero))
'''
#numero 7
'''
numero = int(input("ingrese el numero que quiera saber sus pares"))

def imprimir_pares(numero):
    x =1 
    while x <= numero:
        if x % 2 == 0:
            print("el numero",x," es par")
        x = x + 1
'''
