#EJERCICIO 01
# Función recursiva para imprimir números pares del 1 al 100
def imprimir_pares_recursivo(n):
    # Caso base: cuando n llega a 0, la recursión se detiene
    if n > 0:
        # Llamada recursiva para los números restantes
        imprimir_pares_recursivo(n - 1)
        # Si el número actual es par, imprimirlo
        if n % 2 == 0:
            print(n)

# Llamada a la función
print("----------------------------EJERCICIO 01----------------------------")
imprimir_pares_recursivo(100)


#EJERCICIO 02
# Función recursiva para calcular la suma de los números del 1 al n
def suma_hasta_n_recursivo(n):
    # Caso base: cuando n llega a 1, la recursión se detiene
    if n == 1:
        return 1
    # Llamada recursiva para los números restantes y sumarlos
    return n + suma_hasta_n_recursivo(n - 1)

# Llamada a la función
print("----------------------------EJERCICIO 02----------------------------")
resultado = suma_hasta_n_recursivo(10)
print(resultado)


#EJERCICIO 03
# Función recursiva para imprimir una pirámide de números del 1 al n
def imprimir_piramide_recursivo(n, current=1):
    # Verificar si se ha alcanzado el valor final de la pirámide
    if current <= n:
        # Imprimir la fila actual
        print(" ".join(str(i) for i in range(1, current + 1)))
        # Llamada recursiva para la siguiente fila
        imprimir_piramide_recursivo(n, current + 1)

# Llamada a la función
print("----------------------------EJERCICIO 03----------------------------")
imprimir_piramide_recursivo(5)


#EJERCICIO 04
# Función recursiva para imprimir una pirámide invertida de números del 1 al n
def imprimir_piramide_invertida_recursivo(n):
    # Verificar si se ha alcanzado el valor mínimo
    if n > 0:
        # Imprimir la fila actual
        print(" ".join(str(i) for i in range(1, n + 1)))
        # Llamada recursiva para la siguiente fila
        imprimir_piramide_invertida_recursivo(n - 1)

# Llamada a la función
print("----------------------------EJERCICIO 04----------------------------")
imprimir_piramide_invertida_recursivo(5)


#EJERCICIO 05
# Función recursiva para imprimir la tabla de multiplicar del n
def tabla_multiplicar_recursivo(n, multiplicador=1):
    # Verificar si se han impreso todas las filas
    if multiplicador <= 10:
        # Imprimir la fila actual de la tabla de multiplicar
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        # Llamada recursiva para la siguiente fila
        tabla_multiplicar_recursivo(n, multiplicador + 1)

# Llamada a la función
print("----------------------------EJERCICIO 05----------------------------")
tabla_multiplicar_recursivo(5)

#------------------------------------------------------------------------------
#--------------------------ARREGLO Y MATRICES----------------------------------
#------------------------------------------------------------------------------

#EJERCICIO 06
import numpy as np

# Crear matriz de números reales de 3x3
matriz_reales = np.random.rand(3, 3)
print("----------------------------EJERCICIO 06----------------------------")
print(matriz_reales)


#EJERCICIO 07
# Crear matriz de números complejos de 3x3
matriz_complejos = np.random.rand(3, 3) + 1j * np.random.rand(3, 3)
print("----------------------------EJERCICIO 07----------------------------")
print(matriz_complejos)


#EJERCICIO 08
# Crear matriz de matrices de 2x2
matriz_de_matrices = np.array([[np.random.rand(2, 2), np.random.rand(2, 2)],
                               [np.random.rand(2, 2), np.random.rand(2, 2)]])
print("----------------------------EJERCICIO 08----------------------------")
print(matriz_de_matrices)


#EJERCICIO 09
# Acceder al elemento central de la matriz de números reales
elemento_central = matriz_reales[1, 1]
print("----------------------------EJERCICIO 09----------------------------")
print(elemento_central)


#EJERCICIO 10
# Sumar dos matrices de 2x3
matriz1 = np.random.rand(2, 3)
matriz2 = np.random.rand(2, 3)
suma_matrices = matriz1 + matriz2
print("----------------------------EJERCICIO 10----------------------------")
print(suma_matrices)


#EJERCICIO 11
# Multiplicar matriz original de 2x2 por un factor
matriz_original = np.random.rand(2, 2)
factor = 3
matriz_resultante = matriz_original * factor
print("----------------------------EJERCICIO 11---------------------------")
print(matriz_resultante)


#EJERCICIO 12
# Calcular la media de los elementos de la matriz de números reales
media_matriz = np.mean(matriz_reales)
print("----------------------------EJERCICIO 12----------------------------")
print(media_matriz)

#-------------------------------------------------------------------------------
#-----------------------EJERCICIO PARTE 02--------------------------------------
#-------------------------------------------------------------------------------

#EJERCICIO 01
# Crear matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)
print("----------------------------EJERCICIO 01----------------------------")
print(matriz_aleatoria)


#EJERCICIO 02
# Calcular media, mediana y desviación estándar de la matriz aleatoria
media_matriz = np.mean(matriz_aleatoria)
mediana_matriz = np.median(matriz_aleatoria)
desviacion_estandar_matriz = np.std(matriz_aleatoria)

print("----------------------------EJERCICIO 02----------------------------")
print("Media:", media_matriz)
print("Mediana:", mediana_matriz)
print("Desviación estándar:", desviacion_estandar_matriz)


#EJERCICIO 03
# Función para encontrar el elemento máximo de una matriz
def encontrar_maximo(matriz):
    return np.max(matriz)

# Llamada a la función
maximo_elemento = encontrar_maximo(matriz_aleatoria)
print("----------------------------EJERCICIO 03----------------------------")
print("Elemento máximo:", maximo_elemento)


#EJERCICIO 04
# Función para encontrar la submatriz de mayor suma
def encontrar_submatriz_max_suma(matriz):
    submatriz_max = np.zeros((2, 2))
    max_suma = 0

    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            submatriz = matriz[i:i+2, j:j+2]
            suma_submatriz = np.sum(submatriz)

            if suma_submatriz > max_suma:
                max_suma = suma_submatriz
                submatriz_max = submatriz

    return submatriz_max

# Llamada a la función
submatriz_maxima = encontrar_submatriz_max_suma(matriz_aleatoria)
print("----------------------------EJERCICIO 04----------------------------")
print("Submatriz de mayor suma:")
print(submatriz_maxima)


#EJERCICIO 05
# Función para encontrar la matriz de covarianza de dos matrices
def matriz_covarianza(matriz1, matriz2):
    covarianza = np.cov(matriz1, matriz2)
    return covarianza

# Crear dos matrices aleatorias de 3x3
matriz1 = np.random.rand(3, 3)
matriz2 = np.random.rand(3, 3)

# Llamada a la función
matriz_cov = matriz_covarianza(matriz1, matriz2)
print("----------------------------EJERCICIO 05----------------------------")
print("Matriz de covarianza:")
print(matriz_cov)
