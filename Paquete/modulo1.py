class Persona: # Defino la clase Persona
    def __init__(self, nombre, apellido): #Con el constructor defino 2 atributos 
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona): # Creo la sub clase "Cliente", que heredara los atributos nombre y apellido de la clase "Persona"
    def __init__(self, nombre, apellido, edad, genero, dni, correo, direccion):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.genero = genero
        self.dni = dni
        self.correo = correo
        self.direccion = direccion
        self.carrito = []
    
    def __str__(self): #Utilizo el metodo "str" para cuando imprimamos el objeto "Persona" aparezcan sus atributos
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Género: {self.genero}, DNI: {self.dni}, Correo: {self.correo}, Dirección: {self.direccion}"
    
    def realizar_compra(self, producto):
        self.carrito.append(producto)
        print(f"{self.nombre} {self.apellido} ha agregado '{producto}' al carrito.")

    def consultar_compra(self):
        if not self.carrito:
            print(f"{self.nombre} {self.apellido} no ha realizado compras.")
        else:
            print(f"{self.nombre} {self.apellido} ha realizado las siguientes compras:")
            for producto in self.carrito:
                print(f"- {producto}")


class Empleado(Persona):
    def __init__(self, nombre, apellido, correo, area, puesto):
        super().__init__(nombre, apellido)
        self.correo = correo
        self.area = area
        self.puesto = puesto
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}, Area: {self.area}, Puesto: {self.puesto}"