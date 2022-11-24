"""Vamos a crear una clase llamada Persona. Sus atributos son: 
nombre, edad y DNI. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que 
  validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona():
    def __init__(self,nombre,edad,dni) -> None:
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    
    #getters
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_dni(self):
        return self.__dni
    #setters
    def set_nombre(self,nombre):
         self.__nombre=nombre
    def set_edad(self,edad):
        self.__edad=edad
    def set_dni(self,dni):
        self.__dni=dni
        
    def esMayorDeEdad(self):
        return self.get_edad()>18
    
    def mostrar(self):
        print(self.get_nombre())
        print(self.get_edad())
        print(self.get_dni())
        
    
print("*"*40)
print(" "*13,"BIENVENIDO")
print("*"*40)
print("\nINGRESE LOS DATOS DE LA PERSONA:")
nombre=input("Ingrese el nombre de la persona: ")
while True:
    try:
        edad=int(input("Ingrese edad de la persona: "))
        break
    except ValueError: print("DEBE SER UN NUMERO ENTERO!!!")
  
dni=int(input("Ingrese DNI de la persona: "))

individuo=Persona(nombre,edad,dni)
while True:
    desicion=int(input("Este es un menú:\n1) Editar nombre\n2) Editar edad \n3) Editar DNI\n4) Mostrar los datos de la persona\n\nSeleccione una opcion: "))
    if desicion==1:
        nombre1=input("Ingrese el nombre del individuo: ")
        individuo.set_nombre(nombre1)
    if desicion==2:
        edad1=input("Ingrese la edad del individuo: ")
        individuo.set_edad(edad1)
    if desicion==3:
        dni1=input("Ingrese el dni del individuo: ")
        individuo.set_dni(dni)
    if desicion==4:
        individuo.mostrar()
    
    
        
    
    