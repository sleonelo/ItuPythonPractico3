"""5) Diseñar una clase para describir un artículo con los siguientes atributos: código, stock y precio.
Nombre de la clase: articulo
Atributos:
codigo (código del artículo)
nombre (nombre del articulo)
stock (cantidad actual)
precio (precio unitario)
Métodos
cantidad (muestra el stock actual)
precio (muestra el precio)
vender (reduce el stock actual)
comprar (incrementa el stock actual)
Debe diseñar un pequeño programa para registrar las siguientes acciones a un
“grupo” de productos:
 Cargar datos iniciales para al menos 3 productos
 Registrar ventas y compras
 Hacer Consultas de stock y de precio para un producto en
particular"""

class Articulo():
    def __init__(self,codigo,nombre,stock,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.stock=stock
        self.precio=precio
        
    def cantidad(self):
        return(self.stock)
    
    def valor(self):
        #retorna el precio de un producto
        return(self.precio)
    
    def vender(self,venta):
        #reduce el stock actual
        self.stock=self.stock-venta
        return self.stock 
    
    def comprar(self,stock):
        #aumenta el stock actual
        #self.codigo=codigo
        self.stock=stock
        return self.stock
       
print("-"*20)
print("Bienvenido!")
print("-"*20)

listaDeProductos=[]

def menuDeCarga():
        cod=input("ingrese el codigo del producto: ")
        nom=input("ingrese el nombre del producto: ")
        sto=int(input("ingrese el cantidad de productos que ingresan: "))
        prec=int(input("ingrese el precio del producto: "))
        producto=Articulo(cod,nom,sto,prec)
        listaDeProductos.append(producto)
        #print(listaDeProductos[0].codigo)

while True:
    carga_productos=input("Desea cargar productos? \nS/N\n")
    carga_productos=carga_productos.lower()
    
    if carga_productos=="s":
        menuDeCarga()
    else: 
        ventasYcompras=int(input("1)Registrar venta\n2)Registrar compra\n3)Hacer consulta de stock\n4)Buscar precio de producto\n\nSeleccione una opcion: "))
       
        if ventasYcompras==1:
            codigoVenta=input("ingrese el codigo del producto que vendio: ")
            for i in listaDeProductos:
                if codigoVenta==i.codigo:
                    NumeroVentas=int(input("ingrese el cantidad de productos vendidos: "))
                    i.vender(NumeroVentas)
                    #i.stock=i.stock-NumeroVentas
                    #producto.vender(NumeroVentas)
                    print(f"vendio {NumeroVentas} unidades del producto: {i.nombre}\nquedan {i.stock} productos en stock")
        
        elif ventasYcompras==2: 
            cod=input("ingrese el codigo del producto: ")
            # nom=input("ingrese el nombre del producto: ")
            sto=int(input("ingrese el cantidad de productos que ingresan: "))
            # prec=int(input("ingrese el precio del producto: "))
            for i in listaDeProductos:
                if cod==i.codigo:
                    i.comprar(sto)
                    #i.stock=i.stock+sto
                    print(f"Ahora el stock disponible es: {i.cantidad()} productos")
                       
        elif ventasYcompras==3:
            codigoVentaStock=input("ingrese el codigo del producto para ver el stock: ")
            for i in listaDeProductos:
                if codigoVentaStock==i.codigo:
                    print(f"El stock disponible de {i.nombre} es: {i.cantidad()}")
        
        else:
            precioVenta=input("ingrese el codigo del producto para ver el precio: ")
            for i in listaDeProductos:
                if precioVenta==i.codigo:
                    print(f"El precio de {i.nombre} es: ${i.precio}")
#Registrar ventas y compras, Hacer Consultas de stock y de precio para un producto en particular       
        
