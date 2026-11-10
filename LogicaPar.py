import random

# Genera una lista de 10 números enteros aleatorios entre 1 y 100
def generar_lista():
    return [random.randint(1, 100) for _ in range(10)]

# Algoritmo 1: Bubble Sort 
def bubble_sort(lista):
    copia = list(lista)  # Creamos copia para no modificar la lista original
    n = len(copia)
    iteraciones = 0
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteraciones += 1  # Contamos cada vez que se compara una pareja
            if copia[j] > copia[j + 1]:
                # Intercambio de elementos si están desordenados
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                
    return copia, iteraciones

# Algoritmo 2: Selection Sort
def selection_sort(lista):
    copia = list(lista)
    n = len(copia)
    iteraciones = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            iteraciones += 1  # Contamos cada comparación para hallar el menor
            if copia[j] < copia[min_idx]:
                min_idx = j
                
        # Intercambiamos el menor encontrado con la posición actual
        if min_idx != i:
            copia[i], copia[min_idx] = copia[min_idx], copia[i]
            
    return copia, iteraciones

# Algoritmo 3: Insertion Sort
def insertion_sort(lista):
    copia = list(lista)
    n = len(copia)
    iteraciones = 0
    
    for i in range(1, n):
        actual = copia[i]
        pos = i - 1
        while pos >= 0:
            iteraciones += 1  # Contavalmos cada idación al desplazar elementos
            if copia[pos] > actual:
                copia[pos + 1] = copia[pos]
                pos -= 1
            else:
                break
        copia[pos + 1] = actual
        
    return copia, iteraciones

# Algoritmo 4: Bubble Sort 
def bubble_sort_optimizado(lista):
    copia = list(lista)
    n = len(copia)
    iteraciones = 0
    
    for i in range(n - 1):
        hubo_cambio = False  # Bandera para saber si la lista ya está ordenada
        for j in range(n - 1 - i):
            iteraciones += 1
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                hubo_cambio = True
                
        # Si en una pasada completa no hubo intercambios, terminamos antes
        if not hubo_cambio:
            break
            
    return copia, iteraciones

def principal():
    print("=== COMPARADOR DE ALGORITMOS ===")
    original = generar_lista()
    print("\nLista original:", original)
    
    # Menú principal con opciones de algoritmos y salida
    print("\n--- MENÚ ---")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Bubble Sort Optimizado")
    print("5. Salir")
    
    try:
        op1 = int(input("\nPrimer algoritmo (1-5): "))
        if op1 == 5:
            print("Saliendo del programa...")
            return
        op2 = int(input("Segundo algoritmo (1-5): "))
        if op2 == 5:
            print("Saliendo del programa...")
            return
    except ValueError:
        print("Error: Ingresa un número válido.")
        return

    # Validamos que las opciones estén dentro del rango permitido
    if not (1 <= op1 <= 5 and 1 <= op2 <= 5):
        print("Error: Las opciones deben estar entre 1 y 5.")
        return
        
    # Evitamos comparar el mismo algoritmo consigo mismo
    if op1 == op2:
        print("Error: No puedes seleccionar el mismo algoritmo dos veces.")
        return

    # Estructura para mapear el número elegido con su nombre y función
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Bubble Sort Optimizado", bubble_sort_optimizado)
    ]

    nombre1, func1 = algoritmos[op1 - 1]
    nombre2, func2 = algoritmos[op2 - 1]

    # Ejecutamos ambos algoritmos usando copias independientes de la lista original
    lista1, it1 = func1(original)
    lista2, it2 = func2(original)

    # Mostramos los resultados obtenidos por cada método
    print(f"\n--- RESULTADOS ---")
    print(f"{nombre1}: {lista1} | Iteraciones: {it1}")
    print(f"{nombre2}: {lista2} | Iteraciones: {it2}")
    
    # Comparamos cuál de los dos realizó menos iteraciones
    print(f"\n--- COMPARACIÓN ---")
    if it1 < it2:
        print(f"Ganador: {nombre1} ({it1} vs {it2})")
    elif it2 < it1:
        print(f"Ganador: {nombre2} ({it2} vs {it1})")
    else:
        print(f"Empate ({it1} iteraciones)")

if __name__ == "__main__":
    principal()