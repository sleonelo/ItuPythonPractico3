"""4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. """
class Cuenta():
     def __init__(self,tit,cant) -> None:
         self.__titular=tit
         self.__cantidad=cant
        
     #getters
     def get_titular(self):
         return self.__titular
     def get_cantidad(self):
         return self.__cantidad
    #setters
     def set_titular(self,nombre):
         self.__titular=nombre  
     def set_cantidad(self,plata):
         self.__cantidad=plata

def mostrar():
    print(f"el nombre del titular es: {cliente.get_titular()}")
    print(f"\nel dinero depositado es: ${cliente.get_cantidad()}\n")
    
def ingresarDinero(monto):
    if monto<0:
        monto=0
    nuevoMonto=cliente.get_cantidad()+monto
    print(f"\nel dinero en la cuenta ahora es: ${nuevoMonto}\n")
    cliente.set_cantidad(nuevoMonto)

def retirarDinero(montoaretirar):
    cliente.set_cantidad(cliente.get_cantidad()-montoaretirar)
    if cliente.get_cantidad()<1000:
        print("la cuenta esta en rojo... ")
    print(f"el dinero que queda en su cuenta es: ${cliente.get_cantidad()}")


nombre=input("\nIngrese un nombre: ")



cliente=Cuenta(nombre,0)


while True:
    desicion=int(input(f"Que accion desea realizar {nombre}?:\n\n1)Ingresar dinero\n2)Mostrar datos de la cuenta\n3)retirar dinero\n\nSeleccione una opcion:  "))
    
    if desicion==1:
       monto=int(input("Ingrese la cantidad de dinero que desea depositar: $ "))
       ingresarDinero(monto)
        
        
    if desicion==2:
        mostrar()
        
    if desicion==3:
        retiro=int(input("Ingrese la cantidad de dinero que desea retirar: $ "))
        retirarDinero(retiro)
        


   
