
# Crear matriz asientos 3x4 inicializada con 0s
asientos = [[0 for _ in range(4)] for _ in range(3)]

# Pedir fila y columna al usuario
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[f][c] = 1

# Mostrar el estado de la sala
print("Estado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()