from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Punto de arranque del programa
restaurante = Restaurante("Restaurante Sabor Amazónico Tena")

# Creación de productos
producto1 = Producto("Maito de tilapia roja", "Plato típico", 5.50)
producto2 = Producto("Jugo de guayusa", "Bebida", 1.50)
producto3 = Producto("Seco de pollo de Campo", "Almuerzo", 5.00)

# Creación de clientes
cliente1 = Cliente("Kelly Pineida", "2125984751", 4)
cliente2 = Cliente("Juan Espinoza", "1500531478", 2)

# Registro de objetos en el restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información organizada
restaurante.mostrar_resumen()
restaurante.mostrar_productos()
restaurante.mostrar_clientes()
