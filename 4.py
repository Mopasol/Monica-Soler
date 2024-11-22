palabra = input("Ingrese una palabra: ")
repeticiones = int(input("Ingrese un número: "))

#les muestro una opcion de cada uno

#opcion 1 while
cont = 1

while cont <= repeticiones:
    print(palabra, end=' ') #el end lo que hara en este caso es evitar el salto de linea y ponga un espacio al final de cada palabra
    cont +=1 #nunca olvidarce incrementar el contador

print('\n')
#opcion 2 for
for i in range(repeticiones):
    print(palabra, end=' ')

#opcion 3
print('\n')
print((palabra + ' ')*3)

#si recuerdan de clases anteriores la multiplicacion repite el string