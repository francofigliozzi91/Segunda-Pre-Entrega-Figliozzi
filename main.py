from Paquete.modulo1 import *

cliente1 = Cliente("Franco", "Figliozzi", 31, "Masculino", 36683164, "francofigliozzi91@gmail.com", "Ecuador 1230") # Creo el objeto "cliente1"

print(cliente1)

cliente1.realizar_compra("Campera de Cuero")

cliente1.consultar_compra()

empleado1 = Empleado("Juan", "Perez", "juanperez@gmail.com", "Local", "Vendedor")

print(empleado1)