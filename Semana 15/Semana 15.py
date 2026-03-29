# Administrador de Calificaciones de estudiantes que se desee agregar o incluso eliminar.

estudiantes = {}

print("Bienvenido al sistema de calificaciones")
print()

while True:
    print("¿Qué deseas hacer?")
    print("1. Agregar estudiante")
    print("2. Agregar calificación")
    print("3. Ver estudiante")
    print("4. Ver todos")
    print("5. Eliminar estudiante")
    print("6. Salir")
    
    opcion = input("Elige: ")
    
    if opcion == "1":
        nombre = input("Escribe el nombre: ")
        if nombre in estudiantes:
            print("Ya existe")
        else:
            estudiantes[nombre] = []
            print("Listo!")
    
    elif opcion == "2":
        nombre = input("¿De quién? ")
        if nombre in estudiantes:
            nota = float(input("Nota: "))
            estudiantes[nombre].append(nota)
            print("Agregada")
        else:
            print("No existe")
    
    elif opcion == "3":
        nombre = input("¿Quién? ")
        if nombre in estudiantes:
            notas = estudiantes[nombre]
            print(f"Estudiante: {nombre}")
            print(f"Notas: {notas}")
            if len(notas) > 0:
                promedio = sum(notas) / len(notas)
                print(f"Promedio: {promedio}")
        else:
            print("No encontrado")
    
    elif opcion == "4":
        print("\nEstudiantes:")
        for nombre in estudiantes:
            notas = estudiantes[nombre]
            if len(notas) > 0:
                prom = sum(notas) / len(notas)
                print(f"{nombre}: {prom}")
            else:
                print(f"{nombre}: sin notas")
        print()
    
    elif opcion == "5":
        nombre = input("¿Quién eliminar? ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print("Eliminado")
        else:
            print("No existe")
    
    elif opcion == "6":
        print("Adiós")
        break
    
    else:
        print("Opción inválida")
    
    print()
