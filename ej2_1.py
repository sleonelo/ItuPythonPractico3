"""2) Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Para esto utilice la clase Calculadora."""
class Calculador():
    def __init__(self, num1,num2) -> None:
        self.num1=num1
        self.num2=num2
        
    def suma(self):
        return(self.num1+self.num2)
    def resta(self):
        return(self.num1-self.num2)
    def multiplicacion(self):
        return(self.num1*self.num2)
    def division(self):
        return(self.num1/self.num2)

desicion=int(input("Que operacion queres hacer?\n1)suma\n2)resta\n3)multiplicacion\n4)division\n\nSeleccione una: "))    
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
operacion=Calculador(num1,num2)
if desicion==1:
    print(operacion.suma())
if desicion==2:
    print(operacion.resta())
if desicion==3:
    print(operacion.multiplicacion())
if desicion==4:
    print(operacion.division())

    


