# GOMEZ ROGGIO MATEO JOAQUIN - TRABAJO PRACTICO N° 3 - ESTRUCTURAS CONDICIONALES

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: "))
if(edad > 18):
  print("Es mayor de edad")
else:
  print("No es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 


nota = int(input("Ingrese su nota: "))

if(nota >= 6):
  print("Aprobado")
else:
  print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Ingrese un número par: "))
esPar = False

while (esPar == False):
  if(num % 2 == 0):
    esPar = True
    print("Ha ingresado un número par")
  else:
    esPar = False
    print("Por favor, ingrese un número par")
    num = int(input("Ingrese un número par: "))

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece:
# Niño/a: menor de 12 años. 
# Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

match edad:
  case _ if edad < 12:
    print("La categoría del usuario es: Niño/a")
  case _ if 12 <= edad < 18:
    print("La categoría del usuario es: Adolescente")
  case _ if 18 <= edad < 30:
    print("La categoría del usuario es: Adulto/a joven")
  case _ if edad >= 30:
    print("La categoría del usuario es: Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

pw = input("Ingrese una contraseña: ")
pwValida = False

while (pwValida == False):
  if(len(pw) < 8 or len(pw) > 14 ):
    pwValida = False
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    pw = input("Ingrese una contraseña: ")
  else:
    pwValida = True
    print("Ha ingresado una contraseña correcta")

# 6)escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar 
# si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No cumple estrictamente con ninguna de las condiciones de sesgo definidas.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

frase = input("Ingrese una frase: ")

if frase.endswith(("a", "e", "i", "o", "u")):
    print(f"{frase}!")
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla.

nombre = input("Ingrese su nombre: ")
opcion = 0

print("Formas en las que el usuario puede ver su nombre: ")
print("1. Todo en mayúsculas")
print("2. Todo en minúsculas")
print("3. En modo título")

opcion = int(input("Elija una de las opciones anteriores: "))

match opcion:
  case 1: print(nombre.upper())
  case 2: print(nombre.lower())
  case 3: print(nombre.title())
  case _: print("La opción seleccionada no es válida.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = float(input("Ingrese la magnitud del terremoto: "))

match magnitud:
    case _ if magnitud < 3:
        print("Muy leve (imperceptible)")
    case _ if 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    case _ if 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    case _ if 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    case _ if 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    case _ if magnitud >= 7:
        print("Extremo (puede causar graves daños a gran escala)")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día: "))

estacion = ""

# ----- Invierno Norte / Verano Sur -----
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"

# ----- Primavera Norte / Otoño Sur -----
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"

# ----- Verano Norte / Invierno Sur -----
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"

# ----- Otoño Norte / Primavera Sur -----
else:  
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print(f"En el hemisferio {hemisferio}, en la fecha {dia}/{mes}, es {estacion}.")