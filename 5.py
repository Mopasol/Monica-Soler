n = 1
suma_total = 0
while n: #como nuestro bucle espera un True o False, cualquier numero que no sea 0 dara True
    n = float(input("Ingrese un numero: "))
    suma_total += n

print(f"La suma total es: {suma_total}")


#otra manera

n=1 #reseteamos n
suma_total = 0 #reseteamos suma

while n != 0: 
    n = float(input("Ingrese un numero: "))
    suma_total += n

print(f"La suma total es: {suma_total}")

#otra manera

suma_total = 0 #reseteamos suma

while True: 
    n = float(input("Ingrese un numero: "))
    suma_total += n

    if not n: #mismo caso del primer ejemplo, pero le agregamos el not para ingresar cuando n sea 0
        break

print(f"La suma total es: {suma_total}")

