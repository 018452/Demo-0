# promedio

n=int(input("ingrese la cantidad de datos\n"))

acum=0

i=1

for i in range (n):

    dato=int(input(F"ingresa el dato{i+1}\n"))

    acum+= dato

    prom=acum/n

print("El promedio de sus datos es:",prom)