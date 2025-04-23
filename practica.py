# import json
# from datetime import datetime, timedelta

# # Archivo de datos
# ARCHIVO_CREDITOS = 'creditos.json'

# # --- Modelos del sistema de crédito ---
# class CuotaCredito:
#     def __init__(self, id, numero_cuota, valor, fecha_vencimiento, fecha_pago=None):
#         self.id = id
#         self.numero_cuota = numero_cuota
#         self.valor = valor
#         self.fecha_vencimiento = fecha_vencimiento
#         self.fecha_pago = fecha_pago

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'numero_cuota': self.numero_cuota,
#             'valor': self.valor,
#             'fecha_vencimiento': self.fecha_vencimiento.isoformat(),
#             'fecha_pago': self.fecha_pago.isoformat() if self.fecha_pago else None
#         }

#     @staticmethod
#     def from_dict(d):
#         fecha_pago = datetime.fromisoformat(d['fecha_pago']) if d['fecha_pago'] else None
#         return CuotaCredito(
#             id=d['id'],
#             numero_cuota=d['numero_cuota'],
#             valor=d['valor'],
#             fecha_vencimiento=datetime.fromisoformat(d['fecha_vencimiento']),
#             fecha_pago=fecha_pago
#         )

#     def __str__(self):
#         estado = 'Pagada' if self.fecha_pago else 'Pendiente'
#         pago = self.fecha_pago.strftime('%Y-%m-%d') if self.fecha_pago else '---'
#         return f"Cuota {self.numero_cuota}: valor={self.valor:.2f}, vencimiento={self.fecha_vencimiento.date()}, pago={pago} ({estado})"


# class CreditoCompra:
#     def __init__(self, id, compra_id, total_credito, numero_cuotas, fecha_inicio, estado="Pendiente"):
#         self.id = id
#         self.compra_id = compra_id
#         self.total_credito = total_credito
#         self.numero_cuotas = numero_cuotas
#         self.fecha_inicio = fecha_inicio
#         self.estado = estado
#         self.cuotas = []

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'compra_id': self.compra_id,
#             'total_credito': self.total_credito,
#             'numero_cuotas': self.numero_cuotas,
#             'fecha_inicio': self.fecha_inicio.isoformat(),
#             'estado': self.estado,
#             'cuotas': [c.to_dict() for c in self.cuotas]
#         }

#     @staticmethod
#     def from_dict(d):
#         credito = CreditoCompra(
#             id=d['id'],
#             compra_id=d['compra_id'],
#             total_credito=d['total_credito'],
#             numero_cuotas=d['numero_cuotas'],
#             fecha_inicio=datetime.fromisoformat(d['fecha_inicio']),
#             estado=d['estado']
#         )
#         credito.cuotas = [CuotaCredito.from_dict(cd) for cd in d['cuotas']]
#         return credito

#     def generar_cuotas(self):
#         valor_unitario = self.total_credito / self.numero_cuotas
#         self.cuotas = []
#         for i in range(1, self.numero_cuotas + 1):
#             fecha_venc = self.fecha_inicio + timedelta(days=30 * (i - 1))
#             cuota = CuotaCredito(
#                 id=f"{self.id}-{i}",
#                 numero_cuota=i,
#                 valor=round(valor_unitario, 2),
#                 fecha_vencimiento=fecha_venc
#             )
#             self.cuotas.append(cuota)
#         self.actualizar_estado()

#     def actualizar_estado(self):
#         if all(c.fecha_pago for c in self.cuotas):
#             self.estado = 'Pagado'
#         elif any(c.fecha_pago for c in self.cuotas):
#             self.estado = 'Parcial'
#         else:
#             self.estado = 'Pendiente'

#     def __str__(self):
#         texto = (f"Crédito ID={self.id}, Compra={self.compra_id}, total={self.total_credito:.2f}, "
#                  f"cuotas={self.numero_cuotas}, inicio={self.fecha_inicio.date()}, estado={self.estado}\n")
#         for c in self.cuotas:
#             texto += '  ' + str(c) + '\n'
#         return texto

# # --- Serialización JSON ---
# def cargar_creditos(ruta=ARCHIVO_CREDITOS):
#     try:
#         with open(ruta, 'r', encoding='utf-8') as f:
#             datos = json.load(f)
#             return [CreditoCompra.from_dict(d) for d in datos]
#     except FileNotFoundError:
#         return []


# def guardar_creditos(creditos, ruta=ARCHIVO_CREDITOS):
#     with open(ruta, 'w', encoding='utf-8') as f:
#         json.dump([c.to_dict() for c in creditos], f, ensure_ascii=False, indent=4)

# # --- Funciones de interfaz ---
# def generar_id(creditos):
#     return max([int(c.id) for c in creditos], default=0) + 1


# def registrar_credito(creditos):
#     print("\n--- Registrar nuevo crédito ---")
#     compra_id = input("ID de la compra: ")
#     total = float(input("Total del crédito: "))
#     num = int(input("Número de cuotas: "))
#     fecha_str = input("Fecha de inicio (YYYY-MM-DD): ")
#     fecha_inicio = datetime.fromisoformat(fecha_str)
#     nuevo_id = str(generar_id(creditos))
#     credito = CreditoCompra(nuevo_id, compra_id, total, num, fecha_inicio)
#     credito.generar_cuotas()
#     creditos.append(credito)
#     guardar_creditos(creditos)
#     print("Crédito registrado correctamente.\n")


# def listar_creditos(creditos):
#     print("\n--- Listado de créditos (en memoria) ---")
#     if not creditos:
#         print("No hay créditos registrados.")
#     for c in creditos:
#         print(c)


# def pagar_cuota(creditos):
#     print("\n--- Pago de cuota ---")
#     listar_creditos(creditos)
#     cid = input("Ingrese ID del crédito: ")
#     credit = next((c for c in creditos if c.id == cid), None)
#     if not credit:
#         print("Crédito no encontrado.")
#         return
#     for c in credit.cuotas:
#         print(c)
#     num = int(input("Número de cuota a pagar: "))
#     cuota = next((c for c in credit.cuotas if c.numero_cuota == num), None)
#     if not cuota:
#         print("Cuota no encontrada.")
#         return
#     fecha_str = input("Fecha de pago (YYYY-MM-DD): ")
#     cuota.fecha_pago = datetime.fromisoformat(fecha_str)
#     credit.actualizar_estado()
#     guardar_creditos(creditos)
#     print("Pago registrado correctamente.\n")


# def ver_registros(ruta=ARCHIVO_CREDITOS):
#     """
#     Carga y muestra todos los créditos desde el archivo JSON.
#     """
#     creditos = cargar_creditos(ruta)
#     print("\n--- Registros de Créditos (desde archivo) ---")
#     if not creditos:
#         print("No hay registros de créditos.")
#         return
#     for credito in creditos:
#         print(credito)


# def menu():
#     creditos = cargar_creditos()
#     opciones = {
#         '1': registrar_credito,
#         '2': listar_creditos,
#         '3': pagar_cuota,
#         '4': ver_registros,
#         '5': exit
#     }
#     while True:
#         print("Sistema de Créditos:\n"
#               "1) Registrar crédito\n"
#               "2) Listar (en memoria)\n"
#               "3) Registrar pago de cuota\n"
#               "4) Ver registros (desde archivo)\n"
#               "5) Salir")
#         op = input("Seleccione una opción: ")
#         accion = opciones.get(op)
#         if accion:
#             # ver_registros no necesita lista pasada
#             if op == '4':
#                 accion()
#             elif op in ('1', '2', '3'):
#                 accion(creditos)
#             else:
#                 accion()
#         else:
#             print("Opción inválida. Intente de nuevo.\n")

# if __name__ == '__main__':
#     menu()

import json
from datetime import datetime, timedelta

# Archivo de datos
ARCHIVO_CREDITOS = 'creditos.json'

# --- Helpers genéricos ---
def get_json(ruta):
    """Carga datos JSON de un archivo y devuelve lista de dicts."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_json(data, ruta):
    """Guarda lista de dicts en un archivo JSON."""
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def show(items):
    """Muestra en consola cualquier lista de objetos con __str__."""
    for item in items:
        print(item)

# --- Modelos del sistema de crédito ---
class CuotaCredito:
    def __init__(self, id, numero_cuota, valor, fecha_vencimiento, fecha_pago=None):
        self.id = id
        self.numero_cuota = numero_cuota
        self.valor = valor
        self.fecha_vencimiento = fecha_vencimiento
        self.fecha_pago = fecha_pago

    def to_dict(self):
        return {
            'id': self.id,
            'numero_cuota': self.numero_cuota,
            'valor': self.valor,
            'fecha_vencimiento': self.fecha_vencimiento.isoformat(),
            'fecha_pago': self.fecha_pago.isoformat() if self.fecha_pago else None
        }

    @staticmethod
    def from_dict(d):
        pago = datetime.fromisoformat(d['fecha_pago']) if d['fecha_pago'] else None
        return CuotaCredito(
            id=d['id'], numero_cuota=d['numero_cuota'], valor=d['valor'],
            fecha_vencimiento=datetime.fromisoformat(d['fecha_vencimiento']), fecha_pago=pago
        )

    def __str__(self):
        estado = 'Pagada' if self.fecha_pago else 'Pendiente'
        pago = self.fecha_pago.date() if self.fecha_pago else '---'
        return f"Cuota {self.numero_cuota}: {self.valor:.2f} | venc: {self.fecha_vencimiento.date()} | pago: {pago} ({estado})"


class CreditoCompra:
    def __init__(self, id, compra_id, total_credito, numero_cuotas, fecha_inicio, estado="Pendiente"):
        self.id, self.compra_id = id, compra_id
        self.total_credito, self.numero_cuotas = total_credito, numero_cuotas
        self.fecha_inicio, self.estado = fecha_inicio, estado
        self.cuotas = []

    def to_dict(self):
        return dict(
            id=self.id, compra_id=self.compra_id, total_credito=self.total_credito,
            numero_cuotas=self.numero_cuotas, fecha_inicio=self.fecha_inicio.isoformat(),
            estado=self.estado, cuotas=[c.to_dict() for c in self.cuotas]
        )

    @staticmethod
    def from_dict(d):
        c = CreditoCompra(
            id=d['id'], compra_id=d['compra_id'], total_credito=d['total_credito'],
            numero_cuotas=d['numero_cuotas'], fecha_inicio=datetime.fromisoformat(d['fecha_inicio']),
            estado=d['estado']
        )
        c.cuotas = [CuotaCredito.from_dict(x) for x in d.get('cuotas', [])]
        return c

    def generar_cuotas(self):
        cuota_val = self.total_credito / self.numero_cuotas
        self.cuotas = [
            CuotaCredito(
                id=f"{self.id}-{i}", numero_cuota=i,
                valor=round(cuota_val,2),
                fecha_vencimiento=self.fecha_inicio + timedelta(days=30*(i-1))
            ) for i in range(1, self.numero_cuotas+1)
        ]
        self.actualizar_estado()

    def actualizar_estado(self):
        pagos = [c.fecha_pago for c in self.cuotas]
        self.estado = 'Pagado' if all(pagos) else 'Parcial' if any(pagos) else 'Pendiente'

    def __str__(self):
        lineas = [f"Crédito {self.id} | Compra {self.compra_id} | total {self.total_credito:.2f}"
                  f" | cuotas {self.numero_cuotas} | inicio {self.fecha_inicio.date()} | {self.estado}"]
        lineas += [f"  {c}" for c in self.cuotas]
        return "\n".join(lineas)

# --- Operaciones principales usando helpers ---
def cargar_creditos():
    datos = get_json(ARCHIVO_CREDITOS)
    return [CreditoCompra.from_dict(d) for d in datos]


def guardar_creditos(creditos):
    save_json([c.to_dict() for c in creditos], ARCHIVO_CREDITOS)


def generar_id(creditos):
    return str(max((int(c.id) for c in creditos), default=0) + 1)


def registrar_credito(creditos):
    print("\n-- Registrar nuevo crédito --")
    compra = input("ID compra: ")
    tot = float(input("Total crédito: "))
    n = int(input("# cuotas: "))
    fi = datetime.fromisoformat(input("Fecha inicio YYYY-MM-DD: "))
    cid = generar_id(creditos)
    cr = CreditoCompra(cid, compra, tot, n, fi)
    cr.generar_cuotas()
    creditos.append(cr)
    guardar_creditos(creditos)
    print("Crédito guardado.")


def listar_creditos(creditos):
    print("\n-- Listar créditos en memoria --")
    show(creditos)


def pagar_cuota(creditos):
    print("\n-- Pagar cuota --")
    show(creditos)
    cid = input("ID crédito: ")
    cr = next((c for c in creditos if c.id == cid), None)
    if not cr:
        print("Crédito no existe.")
        return
    show(cr.cuotas)
    num = int(input("# cuota: "))
    cuota = next((c for c in cr.cuotas if c.numero_cuota == num), None)
    if not cuota:
        print("Cuota no existe.")
        return
    cuota.fecha_pago = datetime.fromisoformat(input("Fecha pago YYYY-MM-DD: "))
    cr.actualizar_estado()
    guardar_creditos(creditos)
    print("Pago registrado.")


def ver_registros():
    print("\n-- Registros desde archivo --")
    show(cargar_creditos())


def menu():
    creds = cargar_creditos()
    ops = {
        '1': lambda: registrar_credito(creds),
        '2': lambda: listar_creditos(creds),
        '3': lambda: pagar_cuota(creds),
        '4': ver_registros,
        '5': exit
    }
    while True:
        print("\n1) Registrar crédito | 2) Listar en memoria | 3) Pagar cuota | 4) Ver registros | 5) Salir")
        opt = input("Opción: ")
        accion = ops.get(opt)
        if accion:
            accion()
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    menu()
#python "C:\Users\garyg\Downloads\venta_json\venta_json\practica.py"
