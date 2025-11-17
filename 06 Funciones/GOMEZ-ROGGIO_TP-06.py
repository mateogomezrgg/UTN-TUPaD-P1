import math  

# 1. Función para imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    """Imprime un mensaje simple por pantalla."""
    print("Hola Mundo!")

# 2. Función que recibe nombre y devuelve saludo
def saludar_usuario(nombre):
    """Recibe un nombre y devuelve un saludo personalizado."""
    return f"Hola {nombre}!"

# 3. Función para imprimir información personal completa
def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime una frase con los datos personales recibidos."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Funciones para círculo (Área y Perímetro)
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Calcula el perímetro de un círculo dado su radio."""
    return 2 * math.pi * radio

# 5. Función de conversión de tiempo
def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600

# 6. Función tabla de multiplicar (Uso de Estructuras Repetitivas)
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del 1 al 10 para el número dado."""
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# 7. Función operaciones básicas (Retorna Tupla)
def operaciones_basicas(a, b):
    """Devuelve una tupla con suma, resta, multiplicación y división."""
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b if b != 0 else "No definido"
    return (suma, resta, multi, div)

# 8. Función calcular IMC
def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal."""
    return peso / (altura ** 2)

# 9. Función Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# 10. Función promedio
def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números."""
    return (a + b + c) / 3


# --- PROGRAMA PRINCIPAL (Llamadas a las funciones) ---
if __name__ == "__main__":
    print("\n--- EJERCICIO 1 ---")
    imprimir_hola_mundo()

    print("\n--- EJERCICIO 2 ---")
    nombre_usuario = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo) 

    print("\n--- EJERCICIO 3 ---")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    eda = input("Edad: ")
    res = input("Residencia: ")
    informacion_personal(nom, ape, eda, res)

    print("\n--- EJERCICIO 4 ---")
    radio_user = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio_user):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio_user):.2f}")

    print("\n--- EJERCICIO 5 ---")
    segs = int(input("Ingrese cantidad de segundos: "))
    print(f"Son {segundos_a_horas(segs):.4f} horas.")

    print("\n--- EJERCICIO 6 ---")
    num_tabla = int(input("Ingrese un número para ver su tabla: "))
    tabla_multiplicar(num_tabla)

    print("\n--- EJERCICIO 7 ---")
    n1 = float(input("Ingrese primer número: "))
    n2 = float(input("Ingrese segundo número: "))
    resultados = operaciones_basicas(n1, n2)
    print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multi: {resultados[2]}, Div: {resultados[3]}")

    print("\n--- EJERCICIO 8 ---")
    peso = float(input("Ingrese peso (kg): "))
    altura = float(input("Ingrese altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

    print("\n--- EJERCICIO 9 ---")
    grad_c = float(input("Ingrese temperatura en Celsius: "))
    print(f"En Fahrenheit es: {celsius_a_fahrenheit(grad_c)}")

    print("\n--- EJERCICIO 10 ---")
    cal1 = float(input("Ingrese primer número: "))
    cal2 = float(input("Ingrese segundo número: "))
    cal3 = float(input("Ingrese tercer número: "))
    print(f"El promedio es: {calcular_promedio(cal1, cal2, cal3):.2f}")