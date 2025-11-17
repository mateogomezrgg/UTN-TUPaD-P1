# --- EJERCICIO 1: Factorial ---
def calcular_factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    return n * calcular_factorial(n - 1)

# --- EJERCICIO 2: Fibonacci ---
def fibonacci(n):
    """Devuelve el valor de la serie de Fibonacci en la posición n."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- EJERCICIO 3: Potencia ---
def potencia(base, exponente):
    """Calcula base elevado a exponente recursivamente."""
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# --- EJERCICIO 4: Decimal a Binario ---
def decimal_a_binario(n):
    """Convierte entero a binario (string) recursivamente."""
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

# --- EJERCICIO 5: Palíndromo ---
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo sin usar reverse."""
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# --- EJERCICIO 6: Suma de Dígitos (Matemático) ---
def suma_digitos(n):
    """Suma los dígitos de un número usando % y //."""
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# --- EJERCICIO 7: Pirámide de Bloques ---
def contar_bloques(n):
    """Suma recursiva de n + (n-1) + ... + 1."""
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# --- EJERCICIO 8: Contar Ocurrencias de un Dígito ---
def contar_digito(numero, digito_buscado):
    """Cuenta cuántas veces aparece un dígito en un número entero."""
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    
    contador = 1 if ultimo_digito == digito_buscado else 0
    
    return contador + contar_digito(numero // 10, digito_buscado)


# --- BLOQUE PRINCIPAL DE PRUEBAS ---
if __name__ == "__main__":
    print("\n--- 1. FACTORIAL ---")
    num = int(input("Ingrese número para factorial: "))
    print(f"Factorial de {num} es: {calcular_factorial(num)}")
    print("Serie completa:")
    for i in range(1, num + 1):
        print(f"{i}! = {calcular_factorial(i)}")

    print("\n--- 2. FIBONACCI ---")
    pos = int(input("Ingrese posición de Fibonacci: "))
    print(f"Valor en posición {pos}: {fibonacci(pos)}")
    print("Serie completa:")
    for i in range(pos + 1):
        print(fibonacci(i), end=" ")
    print() # Salto de línea

    print("\n--- 3. POTENCIA ---")
    base = 2
    exp = 5
    print(f"{base} elevado a {exp} es: {potencia(base, exp)}")

    print("\n--- 4. BINARIO ---")
    dec = 10
    print(f"{dec} en binario es: {decimal_a_binario(dec)}")
    
    print("\n--- 5. PALÍNDROMO ---")
    palabra = "neuquen"
    print(f"¿'{palabra}' es palíndromo?: {es_palindromo(palabra)}")
    palabra2 = "hola"
    print(f"¿'{palabra2}' es palíndromo?: {es_palindromo(palabra2)}")

    print("\n--- 6. SUMA DE DÍGITOS ---")
    n_suma = 1234
    print(f"Suma de dígitos de {n_suma}: {suma_digitos(n_suma)}")

    print("\n--- 7. PIRÁMIDE DE BLOQUES ---")
    niveles = 4
    print(f"Bloques para {niveles} niveles: {contar_bloques(niveles)}")

    print("\n--- 8. CONTAR DÍGITO ---")
    numero_largo = 12233421
    buscado = 2
    print(f"El {buscado} aparece {contar_digito(numero_largo, buscado)} veces en {numero_largo}")