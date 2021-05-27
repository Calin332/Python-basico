
#ejercicio 1
print("Triangulo Rectangulo")
print("")
numero=int(input("Ingrese la altura del triangulo (numero entero positivo)"  ))
for i in range(numero):
    for a in range(i+1):
        print("*", end="")
    print("")
#fin del ejercicio 1
print("")
print("")
# ejercicio 2
print("lista descendente")
num=int(input("Ingrese un numero entero positivo  "))
# el rango va desde el numero que ingrese hasta el menos 1
for i in range(num,-1,-1):
    print(i, end=",")
#fin del ejercicio 2
print("")
print("")
print("")
# ejercicio 3
print("Numero Primo")
n=int(input("Ingrese un numero entero positivo mayor que 2  "))
for i in range(2,n):
    if n % i ==0:
        break
if(i+1) ==n :
    print (str(n)+" es primo")
else:
     print (str(n)+" no es primo")
#fin del ejercicio 3