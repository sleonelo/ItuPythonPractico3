"""1) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""
class Alumno():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def aprueba(self):
        if self.nota<6:
            print("no aprobo")
        else:print("El alumno aprobo")


while True:
    nombre=input("ingrese nombre: ")
    nota=int(input("ingrese la nota que se saco: "))
    
    estudiante=Alumno(nombre,nota)

    estudiante.aprueba()
    

