# Numero par e imapr:

def par(numero):
    # codigo
    if numero %2==0:
        print("Numero par")
    else:
        print("Numero impar")
        
for i in range(1,5 + 1):
    numero = int(input(f"Numero {i}: "))
    par(numero)
    n1 = int(input("Numero: "))

# Calculadora con funciones:

def sumar(n1,n2):
    return n1 + n2

def restar(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def division(n1,n2):
    if n2 == 0:
        return "Invalido, no se puede dividir entre 0"    
    else:
        return n1 / n2

print("Inicio Calculadora:")   

while True:    
    n1 = int(input("Numero 1: ")) # El n1 y n2 pueden ser llamados de cualquier forma 
    n2 = int(input("Numero 2: ")) # ""      ""     ""     ""     ""     ""     ""    ""
    
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    
    Operacion = int(input("Operacion a asignar: "))
        
    if Operacion == 1:
        print(sumar(n1,n2))
        
    elif Operacion == 2:
        print(restar(n1,n2))
    
    elif Operacion == 3:
        print(multiplicar(n1,n2))
    
    elif Operacion == 4:
        print(division(n1,n2))
        
    elif Operacion == 5:
        print("Saliendo...")
        break
  
# Numero primo y no primo:

def primo_y_no_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):  
        if numero % i == 0:
            return False
    return True

numero = int(input("Numero: "))

if primo_y_no_primo(numero):
    print("Es un numero primo")
else:
    print("No es primo")
    
# Contador de vocales:

def contador_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    for vocal in frase:
        if vocal in vocales:
            contador += 1
    return contador 

frase = str(input("Frase: "))
print(contador_vocales(frase))

# adiviner numero: 
numero_secreto = 5

print("Adivina el numero:")
print("Numero entro el 1-10")
print(" ")

while True:
    
    user = int(input("Numero: "))
    
    if user == numero_secreto:
        print("Correcto:")
        break
    elif user < numero_secreto:
        print("Mas alto")
        
    elif user > numero_secreto:
        print("Mas bajo")
        
    
        