a= 1
b= 1
while True:
    print ("El piso actual es: ", a)
    print ("Ingrese piso de destino: ", b)
    b= int (input())
    if a<b:
        print ("El ascensor esta subiendo")
    elif a>b:
        print ("El ascensor esta bajando")
    else :
        print ("El destino no puede ser el mismo en el que se encuentra")
    a=b