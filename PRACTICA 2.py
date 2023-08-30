#problema 1 
lista =[]
for i in range(1500,2701):
    if i %7 ==0 and i %5 ==0:
        lista.append(i)

print("los numeros son: ")
print(lista)

#problema 2
def construir_patron(filas):
    for i in range(1, filas * 2):
        if i <= filas:
            num_asteriscos = i
        else:
            num_asteriscos = 2 * filas - i
        
        for j in range(num_asteriscos):
            print("*", end=" ")
        print()

construir_patron(5)


#problema 3
lista_numeros=list()

while True :
    inicio = input("desea ingresar un numero? (si/no): ")
    inicio = inicio.strip().lower()

    if inicio == "si":
        n1=int(input("ingrese el numero: "))
        lista_numeros.append(n1)
    elif inicio == "no":
        break 
    else:
        print("opcion invalida elija otra opcion")
        

pares = list()
impares = list()

for num in lista_numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares(num)

print("numeros ingresados : {listado}".format(listado = lista_numeros))
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")


#problema 4
def ingresar_alumnos(n):
    alumnos = []
    for i in range(n):
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} para Alumno {i+1}: "))
            notas.append(nota)
        
        alumno = {"Alumno": f"Alumno {i+1}", "Notas": notas}
        alumnos.append(alumno)

    return alumnos

def mostrar_listado(alumnos):
    print("\nListado de Alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

n = int(input("Ingrese el número de alumnos: "))
lista_alumnos = ingresar_alumnos(n)
mostrar_listado(lista_alumnos)


#problema 5
def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad


numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito: "))
    
cantidad_veces = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad_veces}")


#problema 6
def fibonacci(n):
    a=0
    b=1

    for i in range(n):
        c=a+b
        a=b
        b=c
    return b

for j in range(0,51):
    print(fibonacci(j))



#problema 7
def numero_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

num = int(input("Ingrese un número: "))
if numero_primo(num):
        print(f"{num} es un número primo.")
else:
     print(f"{num} no es un número primo.")

    

#problema 8
def calcular_factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

num = int(input("Ingrese el numero: "))
resultado = calcular_factorial(num)
print(f"El factorial de {num} es {resultado}")



#problema 9
def sin_vocales(cadena):
    vocales = "aeiou"
    palabra_sinvocales = "".join([c for c in cadena if c not in vocales])
    return palabra_sinvocales

texto = input(str("Ingrese el texto: "))
    
texto_sin_vocales = sin_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)

