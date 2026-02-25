# Tarea: Matriz 5x5 con ingreso por consola
# Autor: Milton Guachala
# Descripción: Programa que crea una matriz de 5x5, pide valores al usuario
# y muestra la matriz de forma organizada en tabla

# INICIO
# Crear una matriz de tamaño 5x5
filas = 5
columnas = 5
matriz = []

# Para cada fila desde 0 hasta 4:
for i in range(filas):
    fila = []
    # Para cada columna desde 0 hasta 4:
    for j in range(columnas):
        # Pedir al usuario un número
        numero = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        # Guardar el número en la matriz
        fila.append(numero)
    matriz.append(fila)

# Mostrar "Matriz ingresada:"
print("\nMatriz ingresada:")

# Para cada fila desde 0 hasta 4:
for i in range(filas):
    # Para cada columna desde 0 hasta 4:
    for j in range(columnas):
        # Mostrar el valor
        print(f"{matriz[i][j]:6}", end=" ")
    # Saltar de línea
    print()

# FIN
print("\n¡Programa finalizado!")
