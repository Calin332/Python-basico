#Ejercicio 1
#la contraseña es alejandro20*
contraseña= "alejandro20*"
# el usuario ingresa la contraseña
ingresar=input(str("Introduce la contraseña "))
if contraseña == ingresar.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
print("")
print("")
#Ejerccicio2
nombre=input("¿Como te llamas?  ")
genero=input("¿Cual es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() <"m":
       grupo= "A"
    else:
        grupo="B"
else:
    if nombre.lower()>"n":
         grupo= "A"
    else:
        grupo="B"
print("Perteneces al grupo "+ grupo)
