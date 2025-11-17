import os

NOMBRE_ARCHIVO = "productos.txt"

# --- Crear archivo inicial con productos ---
# Actividad 1: Crear archivo con 3 productos (nombre, precio, cantidad)
def crear_archivo_inicial():
    productos_iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno,450.0,15",
        "Regla,200.0,10"
    ]
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for prod in productos_iniciales:
            archivo.write(prod + "\n")
    print(f"Archivo '{NOMBRE_ARCHIVO}' creado exitosamente.")

# --- Leer archivo y Cargar en Lista de Diccionarios ---
# Leer, procesar con strip y split 
# Cargar en una lista de diccionarios 
def cargar_productos():
    lista_productos = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Crealo primero.")
        return []

    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            linea = linea.strip() 
            if linea:
                datos = linea.split(",") 
                
                producto = {
                    "nombre": datos[0],
                    "precio": float(datos[1]),
                    "cantidad": int(datos[2])
                }
                lista_productos.append(producto)
    return lista_productos

# --- Función auxiliar para mostrar productos ---
# Mostrar con formato específico 
def mostrar_productos(lista_productos):
    print("\n--- Lista de Productos ---")
    for p in lista_productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# --- Agregar producto ---
# Agregar producto sin borrar contenido existente 
def agregar_producto_append():
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    
    nueva_linea = f"{nombre},{precio},{cantidad}\n"
    
    with open(NOMBRE_ARCHIVO, "a") as archivo:
        archivo.write(nueva_linea)
    print("Producto agregado correctamente.")

# --- 5. Buscar producto ---
# Buscar por nombre en la lista de diccionarios
def buscar_producto(lista_productos):
    buscado = input("\nIngrese el nombre del producto a buscar: ").lower()
    encontrado = False
    
    for p in lista_productos:
        if p['nombre'].lower() == buscado:
            print(f"¡ENCONTRADO! -> Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print("Error: El producto no existe.")

# --- Guardar cambios (Sobrescribir) ---
# Sobrescribir el archivo con la lista actualizada
def guardar_todo(lista_productos):
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for p in lista_productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)
    print("Archivo actualizado y guardado correctamente.")

# --- BLOQUE PRINCIPAL ---
def menu():
    crear_archivo_inicial()
    
    while True:
        print("\n--- GESTIÓN DE ARCHIVOS ---")
        print("1. Mostrar productos (lee del archivo)")
        print("2. Agregar producto (modo 'append' directo al archivo)")
        print("3. Buscar producto (en memoria)")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        mis_productos = cargar_productos()
        
        if opcion == "1":
            mostrar_productos(mis_productos)
            
        elif opcion == "2":
            agregar_producto_append()
            
        elif opcion == "3":
            buscar_producto(mis_productos)
            
        elif opcion == "4":
            guardar_todo(mis_productos) 
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()