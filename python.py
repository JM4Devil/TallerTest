# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca

# # Clase hija
# class Carro(Vehiculo):
#     def __init__(self, marca, modelo):
#         super().__init__(marca)   # Llamar al constructor de Vehiculo
#         self.modelo = modelo

#     def mostrar_info(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}")
        

# # Crear objeto y probar
# mi_carro = Carro("Toyota", "Corolla")
# mi_carro.mostrar_info()

# Nivel 1: clase base
# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca

# # Nivel 2: clase intermedia
# class Carro(Vehiculo):
#     def __init__(self, marca, modelo):
#         # Llamar al constructor de Vehiculo
#         super().__init__(marca)
#         self.modelo = modelo

# # Nivel 3: clase final
# class Electrico(Carro):
#     def __init__(self, marca, modelo, bateria):
#         # Llamar al constructor de Carro
#         super().__init__(marca, modelo)
#         self.bateria = bateria

#     def mostrar_info(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Batería: {self.bateria} kWh")

# # Crear objeto y mostrar info
# tesla = Electrico("Tesla", "Model 3", 75)
# tesla.mostrar_info()

# class Vehiculo:
#     def __init__(self,marca,modelo,año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#     def mostrar_info(self):
#         print(f"Marca: {self.marca}")
#         print(f"Modelo: {self.modelo}")
#         print(f"Año: {self.año}")

# class auto(Vehiculo):
#     def __init__(self,cantidad_puertas, marca, modelo, año):
#         super().__init__(marca,modelo,año)
#         self.cantidad_puertas = cantidad_puertas
#     def mostrar_info(self):
#         super().mostrar_info()
#         print(f"cantidad de puertas: {self.cantidad_puertas}")

# class moto(Vehiculo):
#     def __init__(self,cilindrada,marca,modelo,año):
#         super().__init__(marca,modelo,año)
#         self.cilindrada = cilindrada
#     def mostrar_info(self):
#         super().mostrar_info()
#         print(f"Cantidad de cilindraje: {self.cilindrada}")

# auto1 = auto(4, "Toyota", "Corolla", 2022)
# moto1 = moto(250, "Yamaha", "FZ", 2021)

# print(" Información del auto:")
# auto1.mostrar_info()

# print("\n Información de la moto:")
# moto1.mostrar_info()

#3 ejercicio

class Mascota:
    def __init__(self,nombre, edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Raza: {self.raza}")
    
class Perro(Mascota):
    def __init__(self,Nivel_entrenamiento,nombre,edad,raza):
        super().__init__(nombre,edad,raza)
        self.Nivel_entrenamiento = Nivel_entrenamiento
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Entrenamiento {self.Nivel_entrenamiento}")
    def ladrar(self):
        print("guau guau perra!")

class Gato(Mascota):
    def __init__(self,tipo_pelaje,nombre,edad,raza):
        super().__init__(nombre,edad,raza)
        self.tipo_pelaje = tipo_pelaje
    def mostrar_info(self):
            super().mostrar_info()
            print(f"Tipo de pelaje: {self.tipo_pelaje}")
    def maullar(self):
        print("Mauuuuuuuuu!")

perro1 = Perro("duro","medardo",50,"Pastor aleman")
print ("Informacion del perro: ")
perro1.mostrar_info()
perro1.ladrar()

gato1 = Gato("medio", "medarda",3,"Egipcio")
print("\nInformacion del gato: ")
gato1.mostrar_info()
gato1.maullar()

