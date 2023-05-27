from Contructores import *
import msvcrt
from os import system


def funcion_auto(op_vehiculo, nombre_vehiculo, auto):
    codigo = 0
    op_vehiculo = int(op_vehiculo)
    system("cls")
    cantidad = input("Cuantos vehiculos desea insertar: ")
    for i in range(int(cantidad)):
        codigo = codigo + 1
        system("cls")
        print("__" * 10)
        print(f"Datos del {nombre_vehiculo} : {codigo} de {cantidad}")
        marca = input("Inserte la marca del Vehiculo : ")
        modelo = input("Inserte el modelo : ")
        nro_ruedas = input("Inserte el número de ruedas : ")
        if op_vehiculo == 1:
            velocidad = input("Inserte la velocidad en km/h : ")
            cilindrada = input("Inserte la cilindraje en cc : ")
            nro_puestos = input("inserte numero de puestos : ")
            auto.append(Particular(marca, modelo,
                                   nro_ruedas, velocidad, cilindrada, nro_puestos)
                        )
        else:
            if op_vehiculo == 2:
                velocidad = input("Inserte la velocidad en km/h : ")
                cilindrada = input("Inserte la cilindraje en cc : ")
                carga = input("inserte carga maxima en kg : ")
                auto.append(Carga(marca, modelo,
                                  nro_ruedas, velocidad, cilindrada, carga)
                            )

            else:
                if op_vehiculo == 3:
                    tipo_bici = input("indique tipo bicicleta :")
                    auto.append(Bicicleta(marca,
                                modelo, nro_ruedas, tipo_bici))
                else:
                    if op_vehiculo == 4:
                        tipo_bici = input("indique tipo Motocicleta :")
                        nro_radios = input("indique numero de radios :")
                        cuadro = input("Indique cuadro motocicleta :")
                        motor = input("indique tipo motor :")
                        auto.append(Motocicleta(marca, modelo,
                                    nro_ruedas, tipo_bici, nro_radios, cuadro, motor))
    return (auto)


def funcion_mostrar(auto):
    system("cls")
    print("Imprimiendo en pantalla los Vehiculos almacenados en memoria:\n")
    for x in auto:
        print(x)

    print("\n\n\n\n\nPresione una tecla para continuar...")
    msvcrt.getch()


def relaciones():
    system("cls")
    print("Relacion de las instancias : \n")
    motocicleta_temp = Motocicleta(
        "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    print(
        f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta_temp, Vehiculos)}")
    print(
        f"Motocicleta es instancia con relación a Automovil:  {isinstance(motocicleta_temp, Automovil)}")
    print(
        f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta_temp, Particular)}")
    print(
        f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta_temp, Carga)}")
    print(
        f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta_temp, Bicicleta)}")
    print(
        f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta_temp, Motocicleta)}")
    print("\n\n\n\n\nPresione una tecla para continuar...")
    msvcrt.getch()


"""

particular = Particular(1, "Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga(1, "Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta(1, "Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta(1, "BMW", "F800s", 2,
                          "Deportiva", "2T", "Doble Viga", 21)


print("_"*20)
print("\n\n Imprimiento en pantalla los Vehiculos cargados por sistema \n")

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("_"*20)
print("\n\n Imprimiendo en pantalla los Vehiculos ingresados \n")
for x in auto:
    print(x)

print("\n\n")

print("\n\n")

"""
