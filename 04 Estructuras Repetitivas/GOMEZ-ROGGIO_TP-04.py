# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(0, 101):
    print(i, end="\n")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

entero = input("Ingrese un número entero: ")
print(f"El número {entero} tiene {len(entero)} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

total = 0
for i in range(int(input("Ingrese el primer número: "))+1, int(input("Ingrese el segundo número: "))):
    total += i 
print(f"La suma de todos los numeros comprendidos entre los numeros ingresados es: {total}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    total += numero
print(f"La suma total es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for i in range(100 - 1, 0, -1):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
total = 0
for i in range(1, numero + 1):
    total += i
print(f"La suma de todos los números entre 0 y {numero} es: {total}")