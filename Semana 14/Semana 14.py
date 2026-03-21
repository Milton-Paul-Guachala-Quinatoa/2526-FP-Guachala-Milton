def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

nota1 = float(input("Ingresa nota 1: "))
nota2 = float(input("Ingresa nota 2: "))
nota3 = float(input("Ingresa nota 3: "))

resultado = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio es: {resultado:.2f}")