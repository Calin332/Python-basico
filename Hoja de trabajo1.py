print("CALCULADORA DE IMC")
print("")
Estatura = input ("Ingrese su estatura en (MTS) ")
Peso = input ("Ingrese su peso en (KG) ")
print("")
imc =  round(float(Peso)/float(Estatura)**2,2)
print( "Su Indice de Masa Corporal es=", imc)
if (imc<=18.5):
    print("tiene un indice de masa corporal por debajo de lo normal")
elif(imc>=18.5 and imc<=24.9 ):
    print("tiene un indice de masa corporal normal")
elif(imc>=25.0 and imc<=29.9 ):
    print("tiene un indice de masa corporal de sobrepeso")
elif(imc>=30.0 and imc<=34.5 ):
    print("tiene un indice de masa corporal de Obesidad Grado 1")
elif(imc>=35.0 and imc<=39.9 ):
    print("tiene un indice de masa corporal de Obesidad Grado 2")
elif(imc>=40.0  ):
    print("tiene un indice de masa corporal de Obesidad Grado 3")
