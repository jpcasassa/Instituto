# Variables
cant_pacientes = 0
i= 0
tratamientos = 0
menos_de_2_tratamientos = 0
mas_de_2_tratamientos = 0

try:
    #Solicitar cantidad de pacientes
    print("Ingrese el numero de pacientes a registrar: ")
    cant_pacientes = int(input())

    for i in range(1, cant_pacientes+1):
        print("Ingrese la cantidad de tratamientos del paciente: ")
        tratamientos = int(input())

        if tratamientos > 2:
            mas_de_2_tratamientos += 1
        else:
            menos_de_2_tratamientos += 1

except ValueError:
    print("Debe Ingresar solo numeros válidos!")

else:
    print("Resultados:")
    print("La cantidad de pacientes con más de 2 tratamientos es: " + str(mas_de_2_tratamientos))
    print("La cantidad de pacientes con menos de 2 tratamientos es: " + str(menos_de_2_tratamientos))