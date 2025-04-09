# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# # # # # edad = int(input("Indique su edad: "))

# # # # # if edad <= 0:
# # # # #     print("La edad ingresada no es correcta")
# # # # # elif edad >= 18:
# # # # #     print("Es mayor de edad")
# # # # # else:
# # # # #     pass


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# # # # # nota = int(input("Ingrese su nota: "))
# # # # # if nota > 10 or nota < 0:   
# # # # #     print("Por favor, indique una nota correcta")
# # # # # elif nota >= 6:
# # # # #     print("Aprobado")   
# # # # # else: 
# # # # #     print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

# # # # # num = int(input("Ingrese un número par: "))
# # # # # if num % 2 == 0:
# # # # #     print("Ha ingresado un número par, muy bien!")
# # # # # else:
# # # # #     print("Por favor, ingrese un número par ¬¬")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece: Niño, Adolecente, Adulto joven, Adulto

# # # # # edad = int(input("Ingrese su edad: "))
# # # # # if edad <= 0 or edad >= 150:
# # # # #     pass
# # # # # elif edad >= 30:
# # # # #     print("Con esa edad usted pertenece a la categoria ADULTO/A")
# # # # # elif edad < 30 and edad >= 18:
# # # # #     print("Usted es un ADULTO JOVEN")
# # # # # elif edad < 18 and edad >= 12:
# # # # #     print("Usted es un adolecente")
# # # # # elif edad < 12:
# # # # #     print("Usted es un noño/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

# # # # # password = input("Ingrese una contraseña entre 8 y 14 carácteres: ")
# # # # # if len(password) >= 8 and len(password) <= 14:
# # # # #     print("Ha ingresado una contraseña correcta :)")
# # # # # else: 
# # # # #     print("Por favor, ingrese una contraseña válida") 

# 6)escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# # # # # from statistics import mode, median, mean
# # # # # import random

# # # # # numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# # # # # moda = mode(numeros_aleatorios)
# # # # # mediana = median(numeros_aleatorios)
# # # # # media = mean(numeros_aleatorios)
# # # # # print (numeros_aleatorios)
# # # # # print(f"moda = {moda}\nmediana = {mediana}\nmedia = {media}\n")

# # # # # if moda < mediana and mediana < media:
# # # # #     print("Hay sesgo positivo o a la derecha")
# # # # # elif media < mediana and mediana < moda:
# # # # #     print("Hay sesgo Negativo o a la izquierda")
# # # # # elif media == mediana == moda:
# # # # #     print("No hay sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# # # # # palabra = input("Ingrese una palabra: ")
# # # # # ult_letra = palabra[len(palabra)-1]

# # # # # if ult_letra == "a" or ult_letra == "e" or ult_letra == "i" or ult_letra == "o" or ult_letra == "u":
# # # # #     print(f"{palabra}!")
# # # # # else:
# # # # #     print(palabra)

#8)

# # # # # nombre = input("Ingrese su nombre porfavor: ")
# # # # # opcion = int(input("\nIngrese la opción que desea: \n si quiere mayusculas ingrese 1 \n Si quiere minusculas ingrese 2 \n Si quiere la primer letra mayuscula ingrese 3:\n"))

# # # # # if opcion == 1:
# # # # #     print(nombre.upper())
# # # # # elif opcion == 2:
# # # # #     print(nombre.lower())
# # # # # elif opcion == 3:
# # # # #     print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

# # # # # magnitud = float(input("Ingrese la magnitud del terremoto: "))
# # # # # if magnitud <= 0:
# # # # #     pass
# # # # # elif magnitud < 3:
# # # # #     print("Terremoto muy leve: inperceptible")
# # # # # elif magnitud >= 3 and magnitud < 4:
# # # # #     print("Terremoto leve: ligeramente perceptible")
# # # # # elif magnitud >= 4 and magnitud < 5:
# # # # #     print("Terremoto moderado: perceptible pero no causa daños")
# # # # # elif magnitud >= 5 and magnitud < 6:
# # # # #     print("Terremoto fuerte: puede caausar daños en estructuras débiles")
# # # # # elif magnitud >= 6 and magnitud < 7:
# # # # #     print("Terremoto muy fuerte: puede caausar daños significativos")
# # # # # elif magnitud >= 7:
# # # # #     print("Terremoto extremo: Puede causar grandes daños a escala")

# 10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# # # # # hemisferio = input("En qué emisferio se encuentra(N ó S): ")
# # # # # mes = int(input("Ingrese el mes en que se encuentra (1-12): "))
# # # # # dia= int(input("Ingrese que dia del mes es: "))

# # # # # if hemisferio == "N" or hemisferio == "n":
# # # # #     if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or mes >= 2:
# # # # #         print("La estacion es Invierno")
# # # # #     elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
# # # # #         print("La estacion es Primavera")
# # # # #     elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
# # # # #         print("La estacion es Verano")
# # # # #     elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
# # # # #         print("La estacion es Otoño")

# # # # # elif hemisferio == "S" or hemisferio == "s":
# # # # #     if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or mes >= 2:
# # # # #         print("La estacion es Verano")
# # # # #     elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
# # # # #         print("La estacion es Otoño")
# # # # #     elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
# # # # #         print("La estacion es Invierno")
# # # # #     elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
# # # # #         print("La estacion es Primavera")
    

