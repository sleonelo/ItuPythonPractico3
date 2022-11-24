"""4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. """
class Cuenta():
    def __init__(self, nombre, cantidad) -> None:
        self.__nombre=nombre
        self.__cantidad=cantidad
    #getters
    @property
    def nombre(self):
        return self.__nombre
    @property
    def cantidad(self):
        return self.__cantidad
    #setter
    @nombre.setter
    def snombre(self,nombre):
        self.__nombre=nombre
    @cantidad.setter
    def scantidad(self,cantidad):
        self.__cantidad=cantidad
    #metodo mostrar
    def mostrar(self):
        print(self.nombre) 
        print(self.cantidad)
    #metodo para ingresar dinero
    def ingresar(self):
        monto=int(input("Ingrese el dinero a depositar: $"))
        if monto<0:
            monto=0
        else: self.scantidad=(self.cantidad+monto)
        print("El nuevo monto de la cuenta es: $", self.cantidad)
    #metodo retirar
    def retirar(self):
        retiro=int(input("Cuanto quiere retirar: $"))
        self.scantidad=(self.cantidad-retiro)
        print("Su saldo es de: $",self.cantidad)
        
print("BIENVENIDO")
nombre=input("Ingrese nombre de usuario, por favor: ")
cliente=Cuenta(nombre,0)
while True:
    desicion=int(input(f"Hola {nombre} selecciona una de estas opciones:\n1) Ingresar dinero\n2) Retirar dinero\n3) Mostrar datos de la cuenta\n\nSeleccione una de esas opciones por favor: "))
    if desicion==1:
        cliente.ingresar()
    if desicion==2:
        cliente.retirar()
    if desicion==3:
        cliente.mostrar()

    
        
        

        
    
    
        