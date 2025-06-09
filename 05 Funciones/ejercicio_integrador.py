import utilities
# Definición de funciones
def imprimir_matriz(columnas, filas):
    for i in range(filas):
        for j in range(columnas):
            print("x", end=" ")
        print()  


# Programa principal
ancho = utilities.leer_entero_validado("Ingrese el ancho del rectángulo: ", 1)
alto = utilities.leer_entero_validado("Ingrese el alto del rectángulo: ", 1)
imprimir_matriz(ancho, alto)