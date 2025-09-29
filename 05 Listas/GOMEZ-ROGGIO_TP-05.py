# Actividades: 
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas. 
# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

# notas = [7, 5, 8, 9, 6, 10, 4, 3, 2, 1]
# promedio = 0
# acumulador = 0
# notaMayor = 0
# notaMenor = 0

# print("Las notas de los alumnos son las siguientes: ")

# for i in notas:
#   acumulador += i
#   if(i > notaMayor): 
#     notaMayor = i

#   if(i < notaMenor or notaMenor == 0):
#     notaMenor = i

#   print(i)

# promedio = acumulador / 10

# print(f"El promedio de las notas es: {promedio}")

# print(f"La nota más alta fue: {notaMayor}")

# print(f"La nota más baja fue: {notaMenor}")


# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

# productos = []
# for i in range(5):
#     producto = input(f"Ingrese el nombre del producto {i+1}: ")
#     productos.append(producto)

# print("Lista de productos ordenada alfabéticamente:")
# for producto in sorted(productos):
#     print(producto)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

# import random

# numerosAleatorios = []
# for i in range(15):
#   numerosAleatorios.append(random.randint(1,100))
# numerosPares = []
# numerosImpares = []

# for numero in numerosAleatorios:
#   if(numero % 2 == 0):
#     numerosPares.append(numero)
#   else:
#     numerosImpares.append(numero)

# print(f"La cantidad de números pares es: {len(numerosPares)}")
# print(f"La cantidad de números impares es: {len(numerosImpares)}")

# 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

# datos = [1,3,5,3,7,1,9,5,3]
# datosSinRepetidos = []

# for dato in datos:
#     if dato not in datosSinRepetidos:
#         datosSinRepetidos.append(dato)

# print(f"Nueva lista sin datos repetidos: \n{datosSinRepetidos}")    

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

# alumnos = ["Carolina", "Clara", "Nicolas", "Sandra", "Leandro", "Mario", "Mateo", "Mely"]

# while True: 
#   opcion = int(input("Ingrese 1 para agregar un alumno. \nIngrese 2 para quitar un alumno existente. \nIngrese 3 para mostrar la lista actual de alumnos. \n Ingrese cualquier otro número para salir del sistema. \n"))

#   match opcion:
#     case 1: 
#       nuevoAlumno = input("Ingrese el nombre del alumno que desea agregar a la lista: ")
#       alumnos.append(nuevoAlumno)
#       print(f"La lista de alumnos quedó de la siguiente manera: \n{alumnos}")

#     case 2:
#       alumnoAQuitar = input("Ingrese el nombre del alumno que desea eliminar de la lista: ")
#       if alumnoAQuitar in alumnos:
#         alumnos.remove(alumnoAQuitar)
#         print(f"La lista de alumnos quedó de la siguiente manera: \n{alumnos}")
    
#     case 3: 
#       print(f"Lista de alumnos actual: \n{alumnos} \n")

#     case _:
#       print("Opción inválida, saliendo del sistema...")
#       break

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero). 

miLista = [5, 15, 47, 53, 66, 98, 7]
ultimaPosicion = miLista[-1]
nuevaLista = [ultimaPosicion]
for i in range(len(miLista)-1):
  nuevaLista.append(miLista[i])
print(f"Lista original: {miLista}")
print(f"Lista rotada: {nuevaLista}")

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana. 