opcion = 1

while opcion != 0:
    print("Menu")
    print("1) Sumar")
    print("2) Restar")
    print("0) Salir")
    opcion = int (input())

    if opcion == 1:
        print("Ingrese numeero 1")
        num1 = int (input ())
        print("Ingrese numero 2")
        num2 = int (input ())
        print("El resultado es :", num1+num2)
    if opcion == 2:
        print("Ingrese numero 1")
        num1 = int (input())
        print("Ingrese numero 2")
        num2 = int (input())
        print("El resultado es :", num1-num2)
    if opcion == 0:
        print ("Chau")