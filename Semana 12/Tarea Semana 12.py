# Crear matriz de asientos 3x4 (inicializar en 0)
asientos = [[0 for _ in range(4)] for _ in range(3)]

# Pedir al usuario la fila y columna
print("=== RESERVA DE ASIENTOS DE CINE ===")
print("La sala tiene 3 filas (0-2) y 4 columnas (0-3)")
print()

try:
    f = int(input("Ingrese fila (0 a 2): "))
    c = int(input("Ingrese columna (0 a 3): "))
    
    # Validar que los índices estén dentro del rango
    if f < 0 or f > 2 or c < 0 or c > 3:
        print("Error: Índices fuera de rango")
    elif asientos[f][c] == 1:
        print("Error: El asiento ya está reservado")
    else:
        # Marcar el asiento como reservado
        asientos[f][c] = 1
        print(f"\n✓ Asiento {f}-{c} reservado exitosamente")
except ValueError:
    print("Error: Debe ingresar números válidos")
except IndexError:
    print("Error: Índices fuera de rango")

# Mostrar el estado actual de la sala
print("\n=== ESTADO ACTUAL DE LA SALA ===")
print("(0 = Libre, 1 = Reservado)")
print()

for i in range(3):
    print(f"Fila {i}: ", end="")
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
