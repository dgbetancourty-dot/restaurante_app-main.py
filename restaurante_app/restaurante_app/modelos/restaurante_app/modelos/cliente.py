class Cliente:
    """Representa a un cliente del restaurante."""

    def __init__(self, nombre, cedula, mesa):
        self.nombre = nombre
        self.cedula = cedula
        self.mesa = mesa

    def __str__(self):
        return f"{self.nombre} | Cédula: {self.cedula} | Mesa: {self.mesa}"
