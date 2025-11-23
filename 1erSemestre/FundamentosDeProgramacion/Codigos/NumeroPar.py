# numero = 0
# print ("Ingrese un numero: ")
# numero = int (input())
# print ("el numero ingresado es: " , numero)

# if numero >= 0:
#     print ("El número es positivo")
# else:
#     print ("El número es negativo")
# if numero % 2 == 0:
#     print ("El múmero es par")
# else:
#     print ("el número es impar")
edad = 0 
continuar = 1

while continuar == 1:
    print ("Ingrese edad: ")
    edad = int(input())

    if edad >= 18:
        print ("Es Mayor de edad")
        if edad >= 60:
            print ("Es adulto mayor")
            if edad >= 100:
                print ("Es un dinosaurio")
    else:
        print ("Es Menor de Edad")
    print ("Ingrese 1 si desea continuar sino ingrese 0")
    continuar = int(input ())
    if continuar == 0: 
        break
