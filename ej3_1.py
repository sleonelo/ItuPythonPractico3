"""3) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 
 esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad"""
class Persona():
    def __init__(self,nombre,edad,dni) -> None:
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
        
    #getters
    def nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_dni(self):
        return self.__dni
    #setters
    def set_nombre(self,nombre):
        set.__nombre=nombre
    def set_edad(self,edad):
        set.__edad=edad
    def set_dni(self,dni):
        set.__dni=dni
    #mostrar(): Muestra los datos de la persona.
    def mostrar(self):
        print(self.nombre())
        print(self.get_edad())   
        print(self.get_dni()) 
    #esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad
    def esMayorDeEdad(self):
        if self.get_edad()<18:
            return False
        else: return True

print("Ingrese una persona:")
nombre=input("Ingrese un nombre: ")
edad=int(input("Ingrese edad: "))
dni=int(input("Ingrese numero de dni: "))
individuo=Persona(nombre,edad,dni)
desicion=int(input("1) mostrar persona\n2)Es mayor de edad?\nSeleccione una opcion: "))
if desicion==1:
    individuo.mostrar()
else:print(individuo.esMayorDeEdad())

        
        
  
         
    
    