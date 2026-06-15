from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra productos y clientes registrados en el restaurante."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\nPRODUCTOS REGISTRADOS")
        print("-" * 30)
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\nCLIENTES REGISTRADOS")
        print("-" * 30)
        for cliente in self.clientes:
            print(cliente)

    def mostrar_resumen(self):
        print(f"\nRESTAURANTE: {self.nombre}")
        print(f"Total de productos: {len(self.productos)}")
        print(f"Total de clientes: {len(self.clientes)}")
