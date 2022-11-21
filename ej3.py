"""3) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona:
    def __init__(self,nombre,edad,dni) -> None:
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    # metodos getters    
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_dni(self):
        return self.__dni
    # metodos setters 
    def set_nombre(self,nombre):
        self.__nombre=nombre  
    def set_edad(self,edad):
        self.__edad=edad
    def set_dni(self,dni):
        self.__dni=dni    

individuo=Persona("silvio",36,32492649)

def mostrar():
            print(individuo.get_nombre())
            print(individuo.get_edad())
            print(f"{individuo.get_dni()}\n")
            
def esMayorDeEdad(edad):
    if edad>17:
        return True
    else: return False
            

def menu():
    while True:    
        while True:
            try:
                desicion=int(input("\nMenú:\n\n1)Modificar\n2)Obtener\n3)Mostrar datos de la persona\n\nseleccione una opcion:  "))
                break
            except ValueError:print("Debe ingresar un numero!\n")
        
        #print(desicion)
                       
        if desicion==1:
            while True:
                try:
                    desicion1=int(input("Submenú\n\n1)modificar nombre\n2)modificar edad\n3)modificar dni\n\nSeleccione una opcion: "))
                    break
                except ValueError:print("Debe ingresar un numero!\n")
           
            if desicion1==1:
                nombre=input("ingrese un nuevo nombre: ")
                individuo.set_nombre(nombre)
            if desicion1==2:
                while True:
                    try:
                        edad=int(input("ingrese un nuevo edad: "))
                        break
                    except ValueError:print("debe ser un numero")
                individuo.set_edad(edad)
            if desicion1==3:
                while True:
                    try:
                        dni=int(input("ingrese un nuevo dni: "))
                        break
                    except ValueError:print("debe ser un numero")
                individuo.set_dni(dni)
            
        if desicion==2:
            while True:
                try:
                    desicion2=int(input("Submenú\n\n1)mostrar nombre\n2)mostrar edad\n3)mostrar dni\n\nSeleccione una opcion: "))
                    break
                except ValueError:print("Debe ingresar un numero!\n")
        
            if desicion2==1:
                print(individuo.get_nombre())
            if desicion2==2:
                print(individuo.get_edad())
            if desicion2==3:
                print(individuo.get_dni())
            print(f"es mayor de edad: {esMayorDeEdad(individuo.get_edad())}")
        if desicion==3:
            mostrar()
            print(f"es mayor de edad: {esMayorDeEdad(individuo.get_edad())}")   
menu()        
    
        
