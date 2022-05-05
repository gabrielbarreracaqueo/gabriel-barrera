#tarea 1
payasos = int(input("ingresar la cantidad de payasos:"))
munecas = int(input("ingresar la cantidad de muñecas:"))
vendidos = (payasos + munecas)
resultado = ((payasos*112)+(munecas*75))
print("Peso del paquete entre payasos y munecas");print(resultado)
print("Cantidad de payasos y munecas vendidos");print(vendidos)

#ejercicio2
peso = float(input("Ingrese su peso en Kilogramos:"))
estatura = float(input("Ingrese su estatura en metros:"))
imc = ((peso)/((estatura)**2))
print("Su Indice de Masa Corporal es:")
print(round(imc,2))
