from funcionesv2 import *
from Contructores import *
import msvcrt
from os import system
import csv


def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "a", newline="")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerow(datos)
    archivo.close()


def recuperar(nombre_archivo):
    try:
        vehiculos_dato = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehi in archivo_csv:
            vehiculos_dato.append(vehi)
        archivo.close()
        return vehiculos_dato
    except FileNotFoundError:
        print("archivo no encontrado contacte al administrador o guarde archivo antes!")
        print("\n\n\n\n\nPresione una tecla para continuar...")
        msvcrt.getch()
        return "Error"
