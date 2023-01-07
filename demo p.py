#Ejem1=Suma
cont=0
acum=0
veces=int(input("Digite el numero de veces que desea SUMAR \n"))
while cont<veces:
    tiki=int(input("Digite el primer numero que desea SUMAR \n"))
    pereza=int(input("Digite el segundo numero que desea SUMAR \n"))
    r3=tiki+pereza
    acum=acum+r3
    cont=cont+1
    print("El resultado de la SUMA es: ", r3)
    print("El numero de operacion es: ", cont)
    print("El resultado de la acumulacion es: ", acum)


#Ejem2=Resta
cont=0
acum=0
veces=int(input("Digite el numero de veces que desea RESTAR \n"))
while cont<veces:
    tiki=int(input("Digite el primer numero que desea RESTAR \n"))
    pereza=int(input("Digite el segundo numero que desea RESTAR \n"))
    r3=tiki-pereza
    acum=acum+r3
    cont=cont+1
    print("El resultado de la RESTA es: ", r3)
    print("El numero de operacion es: ", cont)
    print("El resultado de la acumulacion es: ", acum)


#Ejem3=Multipliacion   
cont=0
acum=0
veces=int(input("Digite el numero de veces que desea MULTIPLICAR \n"))
while cont<veces:
    tiki=int(input("Digite el primer numero que desea MULTIPLICAR \n"))
    pereza=int(input("Digite el segundo numero que desea MULTIPLICAR \n"))
    r3=tiki*pereza
    acum=acum+r3
    cont=cont+1
    print("El resultado de la MULTIPLICACION es: ", r3)
    print("El numero de operacion es: ", cont)
    print("El resultado de la acumulacion es: ", acum)


#Ejem4=Division
cont=0
acum=0
veces=int(input("Digite el numero de veces que desea DIVIDIR \n"))
while cont<veces:
    tiki=int(input("Digite el primer numero que desea DIVIDIR \n"))
    pereza=int(input("Digite el segundo numero que desea DIVIDIR \n"))
    r3=tiki/pereza
    acum=acum+r3
    cont=cont+1
    print("El resultado de la DIVICION es: ", r3)
    print("El numero de operacion es: ", cont)
    print("El resultado de la acumulaciones:",acum)