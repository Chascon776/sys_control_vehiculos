
"""inicio clases"""


class Vehiculos:
    """ clase padre"""

    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        """imprime en caso de ser necesario solo la clase padre"""
        mensaje = f"Datos Vehiculos: Marca={self.marca} , Modelo={self.modelo}, numero de ruedas={self.num_ruedas}"
        return mensaje


class Automovil(Vehiculos):
    """Clase hija de vehiculos"""

    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        """imprime la clase padre + hijo"""
        mensaje = f"Automóvil  Marca={self.marca} , Modelo={self.modelo} , Ruedas={self.num_ruedas} , Km/h={self.velocidad} , cc={self.cilindrada}"
        return mensaje


class Bicicleta(Vehiculos):
    def __init__(self,  marca, modelo, num_ruedas, tipo_bici):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bici = tipo_bici

    def __str__(self):
        """imprime la clase padre + hijo"""
        mensaje = f"Bicicleta: Marca={self.marca} , Modelo={self.modelo} ,  Ruedas={self.num_ruedas} , tipo={self.tipo_bici}"
        return mensaje

# hijos Automovil


class Carga(Automovil):
    def __init__(self,  marca, modelo, num_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        """imprime la clase padre + hijo"""
        mensaje = f"Automovil Carga: Marca={self.marca} , Modelo={self.modelo} , Ruedas={self.num_ruedas} , Km/h={self.velocidad} , cc={self.cilindrada} , Carga={self.carga} Kg "
        return mensaje


class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        """imprime la clase padre + hijo"""
        mensaje = f"Automóvil Particular: Marca={self.marca} , Modelo={self.modelo} , Ruedas={self.num_ruedas} , Km/h={self.velocidad} , cc={self.cilindrada} , Nro Puestos={self.nro_puestos}"
        return mensaje


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bici, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, num_ruedas, tipo_bici)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        mensaje = f"Motocicleta: Marca={self.marca}, Modelo={self.modelo},Ruedas={self.num_ruedas}, nro radios={self.nro_radios}, Cuadro={self.cuadro}, motor={self.motor}"
        return mensaje


"""
auto1 = Automovil( "toyota", "yaris", 4, 120, 800)
auto2 = Automovil( "Fiat", "Palio", 4, 95, 1200)
auto3 = Automovil( "Ford", "Fiesta", 4, 125, 1500)


print(auto1.datosauto(), "\n")
print(auto2.datosauto(), "\n")
print(auto2.datosauto(), "\n")
"""
