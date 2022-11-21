"""1) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""


class Alumno():
    def __init__(self):
        self.nombre="individuo"
        self.nota=10
        
    def estado_nota(self):
        if (self.nota>5):
            return "el alumno ha aprobado"
        else: return "el alumno no aprobo"
    
        
olmos=Alumno()
olmos.nombre=input("ingrese un nombre: ")
olmos.nota=int(input(f"ingrese la nota que {olmos.nombre} se saco: "))
print(f"El alumno {olmos.nombre} saco {olmos.nota} por lo tanto {olmos.estado_nota()}")    
