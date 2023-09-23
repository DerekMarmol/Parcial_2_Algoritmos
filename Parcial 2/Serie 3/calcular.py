tipo = input("Ingrese el nombre de la figura a calcular: A:Circulo, B:Rectangulo, C:Triangulo: ")

if tipo == "A":
    print("Ingrese el siguiente dato: ")
    Radio = float(input("Radio:"))
    circulo = 3.1416 * Radio ** 2
    print("El área del círculo es:", circulo)
elif tipo == "B":
    print("Ingrese el siguiente dato: ")
    Alto = float(input("Alto:"))
    Ancho = float(input("Ancho:"))
    rectangulo = Alto * Ancho
    print("El área del rectángulo es:", rectangulo)
elif tipo == "C":
    print("Ingrese el siguiente dato: ")
    Base = float(input("Base:"))
    Altura = float(input("Altura:"))
    triangulo = (Base * Altura) / 2
    print("El área del triángulo es:", triangulo)
else:
    print("Opción no válida.")
