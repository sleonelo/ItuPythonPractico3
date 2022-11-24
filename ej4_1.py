"""4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. """

class Cuenta():
    def __init__(self, titular, cantidad):
        self.__titular=titular
        self.__cantidad=cantidad
    #getters
    def get_titular(self):
        return self.__titular
    def cantidad(self):
        return self.__cantidad
    #setters
    def set_nombre(self,titular):
        self.__titular=titular
    def set_cantidad(self,cantindad):
        self.__cantidad=cantindad
    #Mostrar los datos de la cuenta
    def mostrar(self):
        print(self.get_titular())   
        print(self.cantidad()) 
    #ingresar dinero
    def ingresar(self):
        cantidad=int(input("Ingrese dinero a depositar: $"))
        if cantidad<0:
            self.set_cantidad(self.cantidad())
        else: self.set_cantidad(cantidad+self.cantidad())
        print(f"El nuevo monto de la cuenta se {self.cantidad()}")
    #retirar dinero
    def retirar(self):
        cantidad=int(input("Ingrese dinero a retirar: $"))
        self.set_cantidad(self.cantidad()-cantidad)
        print(f"El dinero restante en la cuenta es: {self.cantidad()}")
        
titular=input("Buen dia! por favor ingrese su nombre de usuario: ")
print(f"*"*40,"\n"," "*13,"BIENVENIDO","\n","*"*40)
cliente=Cuenta(titular,0)
while True:    
    decision=int(input(f"Señor {titular} seleccione una opcion: \n1) Ingresar dinero\n2) Retirar dinero\n3) Ver estado de la cuenta\n\nSeleccione un numero por favor: "))
    if decision==1:
        #ingresoplata=int(input("Ingrese el monto a depositar: $"))
        cliente.ingresar()
    if decision==2:
        #egresoplata=int(input("Ingrese el monto a retirar: $"))
        cliente.retirar()
    if decision==3:
        cliente.mostrar()
    

        
    

    