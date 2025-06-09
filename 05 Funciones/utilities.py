def leer_entero_validado(mensaje, min = float("-inf"), max = float("inf")):
    n = int(input(f"{mensaje}"))
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

def imprimir_mensaje(mensaje):
    print(mensaje)

def imprimir_hola_mundo():
    imprimir_mensaje("Hola, mundo!")

def saludar_usuaruio(nombre):
    nombre = input("Ingrese su nombre: ") 
    imprimir_mensaje(f"Hola, {nombre}!")

def leer_dato(mensaje):
    dato = input(mensaje)
    return dato

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    print(f"El área del círculo es: {area}cm")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(f"El perímetro del círculo es: {perimetro}cm")

def segundos_a_horas(seg):
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = seg % 60
    print(f"{seg} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")

    
def tabla_multiplicar(n):
    for i in range(11):
        print(f"{n} x {i} = {n*i}")
        i += 1


