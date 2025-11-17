# 1. Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario tras agregar frutas:", precios_frutas)

# 2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario tras actualizar precios:", precios_frutas)

# 3. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista_nombres_frutas = list(precios_frutas.keys())
print("Lista solo de frutas:", lista_nombres_frutas)


# --- EJERCICIO 4: Agenda Telefónica ---
#   Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe
print("\n--- EJERCICIO 4: Agenda Telefónica ---")

agenda_tel = {}

print("Ingresa 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    numero = input(f"Número de teléfono: ")
    agenda_tel[nombre] = numero

print("\n--- Consulta ---")
busqueda = input("Ingrese el nombre a buscar: ")

resultado = agenda_tel.get(busqueda, "El contacto no existe.")
print(f"Número: {resultado}")


# # --- EJERCICIO 5: Contador de Palabras ---
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra
print("\n--- EJERCICIO 5: Análisis de Frase ---")

frase = input("Ingresá una frase: ").lower()
palabras = frase.split() 

palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Recuento: {conteo_palabras}")


# --- EJERCICIO 6: Alumnos y Promedios  ---
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
print("\n--- EJERCICIO 6: Notas de Alumnos ---")

registro_alumnos = {}

for i in range(3):
    nombre_alum = input(f"Nombre del alumno {i+1}: ")
    print(f"Ingrese las 3 notas para {nombre_alum}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    registro_alumnos[nombre_alum] = (n1, n2, n3)

print("\n--- Promedios ---")
for alumno, notas in registro_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")


# --- EJERCICIO 7: Operaciones con Sets (Conjuntos) ---
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

print("\n--- EJERCICIO 7: Listas de Aprobados ---")
aprobados_parcial_1 = {101, 102, 103, 104, 105} # Legajos
aprobados_parcial_2 = {103, 104, 105, 106, 107}

print(f"Aprobados P1: {aprobados_parcial_1}")
print(f"Aprobados P2: {aprobados_parcial_2}")

ambos = aprobados_parcial_1 & aprobados_parcial_2
print(f"Aprobaron ambos: {ambos}")

solo_uno = aprobados_parcial_1 ^ aprobados_parcial_2
print(f"Aprobaron solo uno: {solo_uno}")

al_menos_uno = aprobados_parcial_1 | aprobados_parcial_2
print(f"Total de alumnos que aprobaron algo: {al_menos_uno}")


# --- EJERCICIO 8: Control de Stock ---
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

print("\n--- EJERCICIO 8: Stock de Productos ---")

stock_productos = {"Monitor": 10, "Teclado": 20} 

while True:
    print("\n1. Consultar Stock | 2. Agregar Stock | 3. Nuevo Producto | 4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        prod = input("Nombre del producto: ")
        print(f"Stock de {prod}: {stock_productos.get(prod, 'No encontrado')}")
    
    elif opcion == "2":
        prod = input("Nombre del producto: ")
        if prod in stock_productos:
            cantidad = int(input("Cantidad a agregar: "))
            stock_productos[prod] += cantidad
            print(f"Nuevo stock de {prod}: {stock_productos[prod]}")
        else:
            print("El producto no existe, use la opción 3 para crearlo.")

    elif opcion == "3":
        prod = input("Nombre del nuevo producto: ")
        if prod not in stock_productos:
            cantidad = int(input("Stock inicial: "))
            stock_productos[prod] = cantidad
            print("Producto agregado.")
        else:
            print("El producto ya existe.")
            
    elif opcion == "4":
        break

# --- Ejercicio 9: Agenda de eventos ---
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
print("\n--- EJERCICIO 9: Eventos por Día y Hora ---")

agenda_eventos = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("lunes", "14:00"): "Almuerzo con cliente",
    ("martes", "09:00"): "Revisión de código",
    ("viernes", "18:00"): "Salida recreativa"
}

print("Consulta de agenda:")
dia = input("Día (ej: lunes): ").lower()
hora = input("Hora (ej: 10:00): ")

clave_busqueda = (dia, hora) 

if clave_busqueda in agenda_eventos:
    print(f"Evento encontrado: {agenda_eventos[clave_busqueda]}")
else:
    print("No hay eventos agendados para ese horario.")

# --- Ejercicio 10: Países y Capitales ---
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

print("\n--- EJERCICIO 10: Países y Capitales ---")

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París"
}
print(f"Original: {paises_capitales}")

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"Invertido: {capitales_paises}")