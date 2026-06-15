class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
