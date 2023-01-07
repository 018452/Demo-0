#Programa de Menú#

print("Bienvenidos a Tiki-Tiki Store")

i=1

for i in range(4):
    print("Paquetes de recargas:")
    print("Opción 1: 100 diamantes")
    print("Opción 2: 300 diamantes")
    print("Opción 3: 500 diamantes")
    print("Opción 4: 1000 diamantes")
    print("Escoja un paquete de recarga:")
    var1=input()
    print("¿Desea agregar otro paquete?(Si(1)/No(2))")
    var2=int(input())
    if var2==1: 
        print("¿Qué paquete desea agregar?")
    else: 
        break
print("Su recarga se ha realizado con éxito.")