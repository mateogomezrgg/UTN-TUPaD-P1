# Actividades: 
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas. 
# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

notas = [7, 5, 8, 9, 6, 10, 4, 3, 2, 1]
promedio = 0
acumulador = 0
notaMayor = 0
notaMenor = 0

print("Las notas de los alumnos son las siguientes: ")

for i in notas:
  acumulador += i
  if(i > notaMayor): 
    notaMayor = i

  if(i < notaMenor or notaMenor == 0):
    notaMenor = i

  print(i)

promedio = acumulador / 10

print(f"El promedio de las notas es: {promedio}")

print(f"La nota más alta fue: {notaMayor}")

print(f"La nota más baja fue: {notaMenor}")


# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

print("Lista de productos ordenada alfabéticamente:")
for producto in sorted(productos):
    print(producto)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

import random

numerosAleatorios = []
for i in range(15):
  numerosAleatorios.append(random.randint(1,100))
numerosPares = []
numerosImpares = []

for numero in numerosAleatorios:
  if(numero % 2 == 0):
    numerosPares.append(numero)
  else:
    numerosImpares.append(numero)

print(f"La cantidad de números pares es: {len(numerosPares)}")
print(f"La cantidad de números impares es: {len(numerosImpares)}")

# 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

datos = [1,3,5,3,7,1,9,5,3]
datosSinRepetidos = []

for dato in datos:
    if dato not in datosSinRepetidos:
        datosSinRepetidos.append(dato)

print(f"Nueva lista sin datos repetidos: \n{datosSinRepetidos}")    

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

alumnos = ["Carolina", "Clara", "Nicolas", "Sandra", "Leandro", "Mario", "Mateo", "Mely"]

while True: 
  opcion = int(input("Ingrese 1 para agregar un alumno. \nIngrese 2 para quitar un alumno existente. \nIngrese 3 para mostrar la lista actual de alumnos. \n Ingrese cualquier otro número para salir del sistema. \n"))

  match opcion:
    case 1: 
      nuevoAlumno = input("Ingrese el nombre del alumno que desea agregar a la lista: ")
      alumnos.append(nuevoAlumno)
      print(f"La lista de alumnos quedó de la siguiente manera: \n{alumnos}")

    case 2:
      alumnoAQuitar = input("Ingrese el nombre del alumno que desea eliminar de la lista: ")
      if alumnoAQuitar in alumnos:
        alumnos.remove(alumnoAQuitar)
        print(f"La lista de alumnos quedó de la siguiente manera: \n{alumnos}")
    
    case 3: 
      print(f"Lista de alumnos actual: \n{alumnos} \n")

    case _:
      print("Opción inválida, saliendo del sistema...")
      break

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

temperaturas = [
  [15, 28], # Lunes
  [17, 30], # Martes
  [14, 25], # Miércoles
  [13, 27], # Jueves
  [16, 29], # Viernes
  [18, 31], # Sábado
  [19, 32]  # Domingo
]

sumaMinimas = 0
sumaMaximas = 0
amplitudMayor = 0
diaAmplitudMayor = ""
diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for i in range(len(temperaturas)):
  sumaMinimas += temperaturas[i][0]
  sumaMaximas += temperaturas[i][1]
  amplitud = temperaturas[i][1] - temperaturas[i][0]
  if(amplitud > amplitudMayor):
    amplitudMayor = amplitud
    diaAmplitudMayor = diasSemana[i]
promedioMinimas = sumaMinimas / 7
promedioMaximas = sumaMaximas / 7
print(f"El promedio de las temperaturas mínimas es: {promedioMinimas}")
print(f"El promedio de las temperaturas máximas es: {promedioMaximas}")
print(f"El día con mayor amplitud térmica fue el {diaAmplitudMayor} con una amplitud de {amplitudMayor} grados.")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

notas = [
  [7, 8, 9], 
  [6, 5, 7],
  [8, 9, 10],
  [5, 6, 4],
  [9, 8, 7]
]

for i in range(len(notas)):
  promedioEstudiante = sum(notas[i]) / len(notas[i])
  print(f"El promedio del estudiante {i+1} es: {promedioEstudiante}")
for j in range(len(notas[0])):
  sumaMateria = 0
  for i in range(len(notas)):
    sumaMateria += notas[i][j]
  promedioMateria = sumaMateria / len(notas)
  print(f"El promedio de la materia {j+1} es: {promedioMateria}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

tablero = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

print("Tablero inicial:")
for fila in tablero:
    print(fila)

jugador = "X"
ganador = None  # todavía no existe ningún ganador

for turno in range(9):
    print(f"\nTurno del jugador {jugador}")
    
    fila = int(input("Ingresá la fila (1, 2 o 3): ")) - 1
    columna = int(input("Ingresá la columna (1, 2 o 3): ")) - 1
    
    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada. Perdés el turno.")
    
    for fila_tablero in tablero:
        print(fila_tablero)
    
    # Revisar filas para controlar si hay algun ganador
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            ganador = jugador
            break
    
    # Revisar columnas para controlar si hay algun ganador
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] != "-":
            ganador = jugador
            break
    
    # Revisar diagonales para controlar si hay algun ganador
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
        ganador = jugador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
        ganador = jugador
    
    # Si hay ganador, salir del bucle
    if ganador:
        print(f"\n¡El jugador {ganador} ganó.!")
        break
    
    # Cambiar de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

# Si nadie ganó después de 9 turnos
if not ganador:
    print("\nEmpate.!")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana. 

ventas = [
  [150, 200, 250, 300, 350, 400, 450], # Producto 1
  [100, 150, 200, 250, 300, 350, 400], # Producto 2
  [200, 250, 300, 350, 400, 450, 500], # Producto 3
  [50, 100, 150, 200, 250, 300, 350]   # Producto 4
]
totalPorProducto = []
totalPorDia = [0]*7
productoMasVendido = 0
cantidadMasVendida = 0
for i in range(len(ventas)):
  totalProducto = sum(ventas[i])
  totalPorProducto.append(totalProducto)
  if totalProducto > cantidadMasVendida:
    cantidadMasVendida = totalProducto
    productoMasVendido = i + 1
  for j in range(len(ventas[i])):
    totalPorDia[j] += ventas[i][j]
diaMayorVenta = totalPorDia.index(max(totalPorDia)) + 1
for k in range(len(totalPorProducto)):
  print(f"El total vendido del producto {k+1} es: {totalPorProducto[k]}")
print(f"El día con mayores ventas totales fue el día {diaMayorVenta} con un total de {max(totalPorDia)} ventas.")
print(f"El producto más vendido en la semana fue el producto {productoMasVendido} con un total de {cantidadMasVendida} ventas.")
