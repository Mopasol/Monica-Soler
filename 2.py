n = int(input("Ingrese un número: ")) #en este caso casteamos entero, porque estamos viendo las tablas de multuplicar

contador = 1 

while contador <= 10:
    print(f"{n} X {contador} = {n*contador}")
    contador +=1

#otra opcion
print("\nOpción 2")
#reutilziamos contador por eso mismo lo reseteamos

contador = 1

while True:
    print(f"{n} X {contador} = {n*contador}")
    contador +=1

    if contador == 11:
        break

#otra opcion
print("\nOpción 3")
#for version corta
for i in range(10):
    print(f"{n} X {i+1} = {n*(i+1)}")

#otra opcion
print("\nOpción 4")
#for version media
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#otra opcion
print("\nOpción 5")
#for version larga
for i in range(1,11,1):
    print(f"{n} X {i} = {n*i}")


