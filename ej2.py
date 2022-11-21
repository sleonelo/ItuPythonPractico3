"""2) Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Para esto utilice la clase Calculadora."""
class Inicio():
    def __init__(self,num1,num2):
        self.num1=int(num1)
        self.num2=int(num2)    

class Calculadora(Inicio):    
    def suma(self):
        return (self.num1+self.num2)
    def resta(self):
        return (self.num1-self.num2)
    def multiplicacion(self):
        return (self.num1*self.num2)
    def division(self):
        return (self.num1/self.num2)
 
num1=int(input("ingrese un numero: "))    
num2=int(input("ingrese otro numero: "))
operacion=Calculadora(num1,num2)
desicion=int(input("ingrese la operacion que desea realizar:\n1) suma\n2) resta\n3) multiplicacion\n4) division\n\nseleccione una opcion_____"))
if (desicion==1):
    print(operacion.suma())
if (desicion==2):
    print(operacion.resta())
if (desicion==3):
    print(operacion.multiplicacion())
if (desicion==4):
    print(operacion.division())

