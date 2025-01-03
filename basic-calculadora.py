
def suma():
    user = float(input("Numero: "))
    user2 = float(input("Numero: "))
    operacion = user + user2
    return operacion

def resta():
    user = float(input("Numero: "))
    user2 = float(input("Numero: "))
    operacion = user - user2
    return operacion

def multiplicacion():
    user = float(input("Numero: "))
    user2 = float(input("Numero: "))
    operacion = user * user2
    return operacion

def division():
    user = float(input("Numero: "))
    user2 = float(input("Numero: "))
    if user2 != 0:
        operacion = user / user2
        return operacion
    else:
        return "Error: No se puede dividir entre cero"

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    user = int(input("Operacion: "))
    if user == 5:
        print("Saliendo...")
        break
    elif user == 1:
        print(f"Resultado: {suma()}")
    elif user == 2:
        print(f"Resultado: {resta()}")
    elif user == 3:
        print(f"Resultado: {multiplicacion()}")
    elif user == 4:
        print(f"Resultado: {division()}")
    else:
        print("Opción no válida. Inténtalo de nuevo.")