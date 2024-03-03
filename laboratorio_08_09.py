#--------------------------------------------------------------------------------
#EJERCICIOS PARTE 01-------------------------------------------------------------
#--------------------------------------------------------------------------------

# 1. Validar la edad de un usuario
# Solicitar la edad del usuario
try:
    edad = int(input("Ingrese su edad: "))
    assert edad >= 0, "La edad no puede ser negativa"
    assert edad <= 100, "La edad no puede ser mayor a 100"
except ValueError:
    print("Error: Debe ingresar un número entero para la edad.")
except AssertionError as e:
    print("Error:", e)

#2. Verificar el tipo de dato de una variable.
# Definir la variable
variable = 5

# Verificar el tipo de dato de la variable
try:
    assert isinstance(variable, str), "La variable no es tipo string"
except AssertionError:
    print("La variable no es tipo string.")
    # Aquí puedes agregar el código para manejar la situación de tipo de dato incorrecto

# 3. Validar el rango de una calificación
try:
    # Solicitar la calificación al usuario
    calificacion = float(input("Ingrese su calificación: "))
    assert 0 <= calificacion <= 100, "La calificación debe estar entre 0 y 100"
except ValueError:
    print("Error: Debe ingresar un número para la calificación.")
except AssertionError as e:
    print("Error:", e)

# 4. Asegurar que una lista no este vacia
# Crear una lista vacía
lista = []

# Asegurar que la lista no esté vacía
try:
    assert len(lista) > 0, "La lista está vacía"
except AssertionError:
    print("La lista está vacía, por favor, agregue elementos antes de continuar.")
    # Aquí puedes agregar el código para manejar la situación de lista vacía

# 5. Validar la igualdad de dos objetos
# Definir los objetos
objeto1 = "Holaa"
objeto2 = "Hola"

try:
    # Verificar la igualdad de los objetos
    assert objeto1 == objeto2, "Los objetos no son iguales"
except AssertionError as e:
    print("Error:", e)

# 6. Asegurar que un ciclo while se ejecuta al menos una vez
contador = 0
while contador < 1:
    contador += 1
assert contador >= 1, "El ciclo while no se ejecutó"

# 7. Asegurar que una función retorna un valor específico
def suma(a, b):
    return a + b
assert suma(2, 2) == 4, "La función suma no retorna el valor esperado"

# 8. Validar el estado de una variable después de una operación.
x = 5
x += 5
assert x == 10, "El estado de la variable x no es el esperado después de la operación"

# 9. Asegurar que un módulo se ha importado correctamente.
try:
    import math
    assert math.sqrt(4) == 2, "El módulo math no se ha importado correctamente"
except ImportError:
    print("El módulo math no se pudo importar")

#--------------------------------------------------------------------------------
#EJERCICIOS PARTE 02-------------------------------------------------------------
#--------------------------------------------------------------------------------
#Tema: Listas enlazadas simples
'''
10. Buscar nodo: Desarrollar el código de buscar nodo en la lista enlazada simple.
11. Suma de Nodos: Implementa una función que sume todos los nodos de una lista enlazada simple.
12. Longitud de la Lista: Crea una función que devuelva la longitud de una lista enlazada simple.
13. Concatenar Listas: Implementa una función que concatene dos listas enlazadas simples.
14. Eliminar Duplicados: Crea una función que elimine los nodos duplicados de una lista enlazada simple.
15. Invertir Lista: Implementa una función que invierta el orden de una lista enlazada simple.
'''

class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
# 10. BUSCAR NODO
    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False

# 11. SUMAR NODOS
    def suma_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# 12. LONGITUD DE LA LISTA
    def longitud_lista(self):
        longitud = 0
        actual = self.cabeza
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud

# 13. CONCATENAR LISTAS
    def concatenar_listas(self, otra_lista):
        if not self.cabeza:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza
        return self

# 14. ELIMINAR DUPLICADOS
    def eliminar_duplicados(self):
        valores = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato in valores:
                previo.siguiente = actual.siguiente
            else:
                valores.add(actual.dato)
                previo = actual
            actual = actual.siguiente
        return self

# 15. INVERTIR LISTA
    def invertir_lista(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo
        return self

#--------------------------------------------------------------------------------
# EJECUTANDO EL PROGRAMA
#--------------------------------------------------------------------------------

# DAMOS EL VALOR DE LA "ListaEnlazadaSimple()" A LA VARIABLE "lista"
lista = ListaEnlazadaSimple()

# Insertamos algunos nodos al principio de la lista
lista.insertar_al_principio(5)
lista.insertar_al_principio(10)
lista.insertar_al_principio(15)

# Imprimimos la lista para verificar su contenido
print("Lista inicial:")
lista.imprimir_lista()

# Probamos la función buscar_nodo
print("¿El nodo que buscamos está en la lista?", lista.buscar_nodo(10))

# Probamos la función suma_nodos
print("La suma de los nodos es:", lista.suma_nodos())

# Probamos la función longitud_lista
print("La longitud de la lista es:", lista.longitud_lista())

# Creamos una segunda lista
lista2 = ListaEnlazadaSimple()
lista2.insertar_al_principio(20)
lista2.insertar_al_principio(25)
# Imprimimos la segunda lista
print("Segunda lista:")
lista2.imprimir_lista()

# Probamos la función concatenar_listas
lista.concatenar_listas(lista2)
print("Lista concatenada:")
lista.imprimir_lista()

# Probamos la función eliminar_duplicados
lista.insertar_al_principio(15)  # Insertamos un valor duplicado
print("Lista con duplicados:")
lista.imprimir_lista()
lista.eliminar_duplicados()
print("Lista sin duplicados:")
lista.imprimir_lista()

# Probamos la función invertir_lista
print("Lista invertida:")
lista.invertir_lista()
lista.imprimir_lista()
