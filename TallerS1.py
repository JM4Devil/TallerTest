import csv
import os
from abc import ABC, abstractmethod

ARCHIVO = "productos.csv"

# Clase Abstracta (Interfaz)

class ProductoBase(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

# Clase base: Producto

class Producto(ProductoBase):
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "precio": str(self.precio),
            "cantidad": str(self.cantidad)
        }

    def mostrar_info(self):
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}"

# Subclases con herencia

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def to_dict(self):
        data = super().to_dict()
        data["fecha_expiracion"] = self.fecha_expiracion
        return data

    def mostrar_info(self):
        return f"{self.nombre} (Alimento) - ${self.precio} - Cantidad: {self.cantidad} - Expira: {self.fecha_expiracion}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia_meses):
        super().__init__(nombre, precio, cantidad)
        self.garantia_meses = garantia_meses

    def to_dict(self):
        data = super().to_dict()
        data["garantia_meses"] = str(self.garantia_meses)
        return data

    def mostrar_info(self):
        return f"{self.nombre} (Electrónico) - ${self.precio} - Cantidad: {self.cantidad} - Garantía: {self.garantia_meses} meses"

# Gestor de productos
##hola
class GestorProductos:
    def __init__(self):
        self.productos: list[ProductoBase] = []
        self.cargar_desde_archivo()

    def agregar_producto(self):
        print("\nTipo de producto:")
        print("1. General")
        print("2. Alimenticio")
        print("3. Electrónico")
        tipo = input("Selecciona tipo (1-3): ")

        nombre = input("Nombre del producto: ").strip()
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print(" Precio y cantidad deben ser válidos.")
            return

        if tipo == "2":
            fecha_exp = input("Fecha de expiración (YYYY-MM-DD): ")
            producto = ProductoAlimenticio(nombre, precio, cantidad, fecha_exp)
        elif tipo == "3":
            try:
                garantia = int(input("Meses de garantía: "))
            except ValueError:
                print(" Garantía debe ser un número entero.")
                return
            producto = ProductoElectronico(nombre, precio, cantidad, garantia)
        else:
            producto = Producto(nombre, precio, cantidad)

        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto agregado correctamente.")

    def ver_productos(self):
        if not self.productos:
            print(" No hay productos.")
            return
        print("\n Lista de productos:")
        for i, p in enumerate(self.productos, 1):
            print(f"{i}. {p.mostrar_info()}")

    def buscar_producto(self):
        nombre = input(" Buscar producto por nombre: ").strip().lower()
        encontrados = [p for p in self.productos if nombre in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p.mostrar_info())
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        nombre = input(" Nombre del producto a eliminar: ").strip().lower()
        original_len = len(self.productos)
        self.productos = [p for p in self.productos if p.nombre.lower() != nombre]

        if len(self.productos) < original_len:
            self.guardar_en_archivo()
            print(" Producto eliminado.")
        else:
            print(" Producto no encontrado.")

    def guardar_en_archivo(self):
        with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["tipo", "nombre", "precio", "cantidad", "fecha_expiracion", "garantia_meses"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            for p in self.productos:
                writer.writerow(p.to_dict())

    def cargar_desde_archivo(self):
        if not os.path.exists(ARCHIVO):
            return
        with open(ARCHIVO, mode="r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                tipo = fila.get("tipo", "Producto")
                nombre = fila["nombre"]
                precio = float(fila["precio"])
                cantidad = int(fila["cantidad"])

                if tipo == "ProductoAlimenticio":
                    producto = ProductoAlimenticio(nombre, precio, cantidad, fila["fecha_expiracion"])
                elif tipo == "ProductoElectronico":
                    producto = ProductoElectronico(nombre, precio, cantidad, int(fila["garantia_meses"]))
                else:
                    producto = Producto(nombre, precio, cantidad)

                self.productos.append(producto)

# Menú principal

def mostrar_menu():
    print("\n--- Menú de Gestión de Productos ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

gestor = GestorProductos()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    match opcion:
        case "1": gestor.agregar_producto()
        case "2": gestor.ver_productos()
        case "3": gestor.buscar_producto()
        case "4": gestor.eliminar_producto()
        case "5":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")