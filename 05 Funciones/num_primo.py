#nombre = input("Coloca tu nombre: ")
# Función para saludar
#print(f"Hola{nombre}")
#print(f"Tu nombre mide {len(nombre)} caracteres")

# definicion de funciones
def leer_entero_validado(mensaje, min = float("-inf"), max = float("inf")):
    n = int(input(f"{mensaje} "))
    while n < min or n > max:
        n = int(input(f"ERROR: {mensaje} "))
    return n

def resto(num1, num2):
    return num1 % num2

def es_multiplo(num1, num2):
    return resto(num1, num2) == 0

def es_primo(numero):
    cont = 2 
    while cont < numero and not es_multiplo(numero, cont):
        cont += 1
    return cont >= numero

def informar_si_es_primo(numero):
    if es_primo(numero):
        print(f"{numero} es primo")       
    else:
        print(f"{numero} NO es primo")

# invocacion de funciones
num = leer_entero_validado("Ingrese un número natural:")
informar_si_es_primo(num)

 