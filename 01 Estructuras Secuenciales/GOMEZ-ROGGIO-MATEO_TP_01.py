import math

# Ejercicio 1:  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo!")


# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 

nombre2 = input("Ingrese su nombre: ")
print(f"Hola {nombre2}! Cómo estás hoy??")


# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarDeResidencia = input("Ingrese su domicilio: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")


# Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro.
pi = math.pi
radio = int(input("Ingrese el radio del circulo: "))
area =  pi * radio**2
perimetro = 2 * radio * pi
print(f"El Área del circulo con radio = {radio}, es de {area}")
print(f"El Perímetro del circulo con radio = {radio}, es de {perimetro}")


# Ejercicio 5:  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.
minutos = int(input("Ingrese la cantidad de minutos que desea convertir a horas: "))
horas = minutos / 60

print(f"La cantidad de horas que corresponden a los {minutos} ingresados es: {horas}")


# Ejercicio 6:   Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  
numero = input("Ingrese un número para ver su tabla de multiplicar: ")

for i in range(1, 11):
    print(f"{numero} x {i} = {int(numero) * i}")

# Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

esNum1Cero = False
esNum2Cero = False

num1 = int(input("Ingrese el primer número: "))
if( num1 == 0):
    esNum2Cero = True

while esNum1Cero:
    num1 = int(input("Ingrese el primer número: "))
    if num1 != 0:
        break
    print("El primer número no puede ser 0. Por favor, ingrese un número distinto de 0.")

num2 = int(input("Ingrese el segundo número: "))
if( num2 == 0):
    esNum2Cero = True

while esNum2Cero:
    num2 = int(input("Ingrese el segundo número: "))
    if num2 != 0:
        break
    print("El segundo número no puede ser 0. Por favor, ingrese un número distinto de 0.")


print(f"La suma de {num1} + {num2} es: {num1 + num2}")
print(f"La resta de {num1} - {num2} es: {num1 - num2}")
print(f"La multiplicación de {num1} * {num2} es: {num1 * num2}")
print(f"La división de {num1} / {num2} es: {num1 / num2}")


# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo: (((ver formula en el pdf. pero es peso en kg / altura en metros al cuadrado!!)))

esAlturaCero = False
pesoEnKg = float(input("Ingrese su peso en kg: "))
alturaEnMetros = float(input("Ingrese su altura en metros: "))

if( alturaEnMetros == 0):
    esAlturaCero = True

while esAlturaCero:
    alturaEnMetros = int(input("Ingrese la altura del usuario ( en metros ): "))
    if alturaEnMetros != 0:
        break
    print("La altura del usuario no puede ser 0. Por favor, ingrese una altura válida.")

imc = pesoEnKg/(alturaEnMetros**2)

print(f"El IMC del usuario es de: {imc}")


# Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: (ver pdf)
# temperatura en fahrenheit = 9/5 * temperatura en celsius + 32

gradosCelsius = int(input("Ingrese la temperatura en Celsius, para ver su equivalente en Fahrenheit: "))
celsiusAFahrenheit = (9/5 * gradosCelsius) + 32

print(f"{gradosCelsius}°C equivalen a {celsiusAFahrenheit}°F.")

# Ejercicio 10: Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números ingresados es: {promedio}")