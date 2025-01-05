# Averigua el area un triagulo:
"""
def trianlugo(b,a): 
    area = (b * a) / 2
    return area

b = int(input("ingrese la base: "))
a = int(input("ingrese la altura: "))

area = trianlugo(b,a)

print(f"El area es {area}")


# Numero par o impar ingresado por el user: 

def par_impar(numero):
    if numero %2==0:
        return "par"
    else:
        return "impar"

numero = int(input("ingrese un numero: "))
argumento = par_impar(numero)
print(f"Numero > {argumento}")


# Grados celsius a Fahrenheit:

def celsius_Fahrenheit(celsius):
    formula = celsius * (9/5) + 32
    return formula

celsius = float(input("ingrese temp, en grados >C<: "))
argumento = celsius_Fahrenheit(celsius)
print(argumento)

# Calculadora bine basica:

def calculadora(num1,num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 !=0:
            return num1 / num2
        else:
            return "Numero incorrecto: No se puede / entre 0"
    else:
        return "Operador incorrecto"
    
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
operador = input("ingrese la Operador a asignar: ")
Operacion = calculadora(num1,num2,operador)
print(f"Operacion = {Operacion}")

# Numero mayor de los 3 parametros ingresados:

def mayor_num(n1,n2,n3):
    mayor = max(n1,n2,n3)
    return mayor

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
numero_mayor = mayor_num(n1,n2,n3)
print(f"El numero mayor es {numero_mayor}")
"""


# Devuelva True si es primo o False si no lo es:

def primo(n):
    for i in range(2,n):
        if i %n==0:
            return False
        else:
            return True
n = int(input("Numero entero: "))
result_final = primo(n)
print(result_final)