from funcionesv2 import *
from Contructores import *
from Archivo import *
import msvcrt
from os import system
global auto
auto = []
auto.append(Particular("Ford", "Fiesta", 4, "180", "500", 5))
auto.append(Motocicleta("BMW", "F800s", 2,
            "Deportiva", "2T", "Doble Viga", 21))
auto.append(Automovil("Ford", "Fiesta", 4, 125, 1500))
auto.append(Automovil("Ford", "Fiesta", 4, 125, 1500))
print(len(auto))
opcion = ""
while opcion != "10":
    system("cls")
    print(f"Cantidad de Vehiculos sin guardar : {len(auto)}")
    opcion = input("Ingrese que desea hacer : \n\n1.-Crear Vehiculo pasajeros\n2.-Crear Vehiculo carga\n3.-Crear Bicicleta\n4.-Crear Motocicleta\n5.-Leer Vehiculos en Memoria\n6.-Escribir Archivo\n7.-Leer Archivo\n8.-Mostrar Relaciones \n9.-Salir\n$>")
    match opcion:
        case "1":
            funcion_auto(1, "Vehiculo de Pasajero", auto)
        case "2":
            funcion_auto(2, "Vehiculo de Carga", auto)
        case "3":
            funcion_auto(3, "Bicicleta", auto)
        case "4":
            funcion_auto(4, "Motocicleta", auto)
        case "5":
            funcion_mostrar(auto)
        case "6":
            for i in auto:
                guardar("vehiculos.csv", i)
            auto.clear()
        case "7":
            automoviles = recuperar("vehiculos.csv")
            if automoviles != "Error":
                system("cls")
                for xx in automoviles:
                    print(xx)
                print("\n\n\n\n\nPresione una tecla para continuar...")
                msvcrt.getch()
        case "8":
            relaciones()
        case "9":
            system("cls")
            print("hasta luego.....")
            print("\n\n\n\n\nPresione una tecla para continuar...")
            msvcrt.getch()
            break
        case  default:
            print("ingrese una opcion valida")
            print("\n\n\n\n\nPresione una tecla para continuar...")
            msvcrt.getch()
