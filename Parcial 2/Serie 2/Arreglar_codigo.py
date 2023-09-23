def mostrar_mensaje(mensaje):

    print("*********************") #Error No.1: Faltaban comillas en el texto
    print(mensaje) #Error No.2 : Fataltaba un parentesis
    print("*********************")


def carga_suma(): #Error No.3: No debe llevar llaves

    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    return suma


# Programa principal #Error No.4: Los comentarios se escriben con "#"

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado:")
suma = carga_suma() #Error No.5: La función carga_suma() no devolvía la suma de los dos valores.
mostrar_mensaje(f"La suma de los dos valores es: {suma}") #Error No. 6: La función mostrar_mensaje() imprimía la suma sin formato.

