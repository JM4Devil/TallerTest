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

#3 ejercicio guardar archivo peroe ste archivo se repite 
#el siguiente ejercicio lo hare con que tenga validaciones para que no se repita

# class Mascota:
#     def __init__(self,nombre, edad,raza):
#         self.nombre = nombre
#         self.edad = edad
#         self.raza = raza
    
#     def mostrar_info(self):
#         print(f"Nombre: {self.nombre}")
#         print(f"Edad: {self.edad}")
#         print(f"Raza: {self.raza}")
    
# class Perro(Mascota):
#     def __init__(self,Nivel_entrenamiento,nombre,edad,raza):
#         super().__init__(nombre,edad,raza)
#         self.Nivel_entrenamiento = Nivel_entrenamiento
#     def mostrar_info(self):
#         super().mostrar_info()
#         print(f"Entrenamiento {self.Nivel_entrenamiento}")
#     def ladrar(self):
#         print("guau guau perra!")

# class Gato(Mascota):
#     def __init__(self,tipo_pelaje,nombre,edad,raza):
#         super().__init__(nombre,edad,raza)
#         self.tipo_pelaje = tipo_pelaje
#     def mostrar_info(self):
#             super().mostrar_info()
#             print(f"Tipo de pelaje: {self.tipo_pelaje}")
#     def maullar(self):
#         print("Mauuuuuuuuu!")

# perro1 = Perro("duro","medardo",50,"Pastor aleman")
# print ("Informacion del perro: ")
# perro1.mostrar_info()
# perro1.ladrar()

# gato1 = Gato("medio", "medarda",3,"Egipcio")
# print("\nInformacion del gato: ")
# gato1.mostrar_info()
# gato1.maullar()

# def guardar_mascota(mascota):
#     with open("mascotas.txt", "w") as archivo:
#         archivo.write(f"Guardando nueva mascota...\n")
#         archivo.write(f"nombre: {mascota.nombre}| Edad: {mascota.edad}| Raza: {mascota.raza}\n")

# guardar_mascota(perro1)
# guardar_mascota(gato1)

#ejercicio 4 ejercicio guardado sin dubplicados y en .json
import json
import os
from abc import ABC, abstractmethod
class Producto():
    def __init__(self,nombre, codigo_barras,precio):
        self.nombre = nombre
        self.codigo_barras = codigo_barras
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Codigo de barra: {self.codigo_barras}")
        print(f"Precio: {self.precio}")
    
    def a_dict(self):
        return {
            "id": self.codigo_barras,
            "nombre": self.nombre,
            "precio": self.precio
        }
    
def guardar_producto_json (producto,archivo ="productos.json"):
    #convertimos el producto a diccionario
    producto_dict = producto.a_dict()

    if not os.path.exists(archivo):
        productos = []
    else:
        with open(archivo, "r") as f:
            try:
                productos = json.load(f)
            except json.JSONDecodeError:
                productos = []
    ids_existentes = [p["id"] for p in productos]
    if producto_dict["id"] not in ids_existentes:
        productos.append(producto_dict)
        with open(archivo, "w") as f:
            json.dump (productos, f, indent=4)
        print("Producto guardado.")
    else:
        print("Este producto ya existe o no se guardo.")

producto1 = Producto("Coca-cola","159753", 8.5)
producto2 = Producto("Pepsi","147852", 7.8)
producto3 = Producto("Coca-cola","159753", 8.5)

guardar_producto_json(producto1)
guardar_producto_json(producto2)
guardar_producto_json(producto3)

#ejercicio 5 es lo mismo que el anterior pero para reforzar 

class Libro():
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
    def mostrar_info(self):
        print(f"Titulo: {self.titulo}") 
        print(f"Autor:{self.autor}")
        print(f"Isbn: {self.isbn}")
    def a_dict(self):
        return{
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn
        }

def guardar_libro_json(libro, archivo = "libro.json"):
    libro_dict = libro.a_dict()

    if not os.path.exists(archivo):
        libros = []
    else:
        with open (archivo, "r") as archive:
            try:
                libros = json.load(archive)
            except json.JSONDecodeError:
                libros = []
    isbn_existentes = [p["isbn"] for p in libros]
    if libro_dict["isbn"] not in isbn_existentes:
        libros.append(libro_dict)
        with open(archivo, "w") as archive:
            json.dump(libros, archive, indent=4)
            print("Libro guardado correctamente.")
    else:
        print("Este libro ya existe o no se guardo")

libro1 = Libro("1984", "George orwell", "159753")
libro2 = Libro("Cien años de soledad", "Gabriel Garcia", "147852")
libro3 = Libro("1984", "George orwell", "159753")

guardar_libro_json(libro1)
guardar_libro_json(libro2)
guardar_libro_json(libro3)

############
#ejercicio 6 polimorfismo añadido y clase abstracta
############
class Publicacion(ABC):
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    @abstractmethod

    def mostrar_info(self):
        pass

    @abstractmethod

    def a_dict (self):
        pass

class Libro(Publicacion):
    def __init__(self, titulo, autor,isbn):
        super().__init__(titulo,autor)    
        self.isbn = isbn
    def mostrar_info(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"isbn: {self.isbn}")
    def a_dict(self):
        return{
            "tipo": "libro",
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn
        }
class Revista(Publicacion):
    def __init__(self, titulo, autor,edicion):
        super().__init__(titulo, autor)
        self.edicion = edicion
    def mostrar_info(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"edicion: {self.edicion}")
    def a_dict(self):
        return{
            "tipo": "revista",
            "titulo": self.titulo,
            "autor": self.autor,
            "edicion": self.edicion
        }
libro1 = Libro("Python para todos","Gary Gallardo", "159753")
revista1 = Revista("Revista de Tecnologia","Ana lopez", "Edicion 101")

publicaciones = [libro1, revista1]

for p in publicaciones:
    p.mostrar_info()

class guardar_publicacion_json(publicaciones, archivo = "publicaciones.json"):
    publicaciones_dict = publicaciones.a_dict()
    if not os.path.exists(archivo):
        publicacioness = []
    else:
        with open(archivo, "r") as archive:
            try: 
                publicacioness = json.load(archive)
            except json.JSONDecodeError:
                publicacioness = []
    