#Programa que procesa los montos del cliente
#Bienvenido al programa
print("Bienvenido a su programa de compras")

#Declarando variables
usuario = input("Ingrese el nombre del vendedor: ")
i = 0
producto = ""
precio = 0
#Variable monto total e item son importante para guardar o imprimir los valores
monto_total = 0
item = ""

#Variable follow es necesaria para el bucle while
follow = "SI"
#Evaluar si el vendedor quiere hacer un registro de venta
print("Quiere hacer un registro de venta:\n1- SI \n2- NO")
follow_master = str(input("Ingrese su opcion: ").upper())

#Evaluando si el vendedor dijo "si" quiere hacer el registro
while follow_master == "SI" or follow_master == "1" :
    #En este bucle se evalua el monto de cada producto con su respectivo descuente si es mayor a 500 o mayor a 1000
    #Y guarda el nombre del producto más su precio con descuento
    while follow == "SI" or follow == "1":
        producto = input("Ingresar su producto: ")
        monto = float(input("Ingresar el precio de su producto: $"))
        while monto < 0:
            if monto < 0:
                print("Monto rechazado.")
            monto=float(input("Ingrese nuevamente el monto de su producto: $"))
            
        #Evaluando el descuento aplicar al monto de cada producto
        if monto > 500:
            descuento = monto * 0.05
            precio = monto - descuento
            
        elif monto >1000:
            descuento = monto * 0.10
            precio = monto - descuento
        else:
            precio = monto

        monto_total += precio
        #En la variable item se guardan en nombre del producto con su respectivo precio
        item += producto +" $"+str(precio)+","
        
        print("Quiere Ingresar mas productos: \n1- SI \n2- NO") 
        #Preguntamos si quiere seguir ingresando más productos
        #Y si no quiere seguir, entonces con el follow cerramos el bucle y con el follow master cerramos la sección del vendedor
        follow = str(input("Ingrese su opcion: ").upper())   
        follow_master = follow
    
    ##"Mostrando nuestro registro de venta"##
    print("==============================================")
    print("=========Lista de productos vendidos==========")
    print("==============================================")
    for x in item.split(','):
        i += 1 
        print(i," ==",x.replace(',','\n'))
    print("==============================================")
    print("El monto total a pagar es de: $",monto_total)
    print("Venta hecha por el empleado ", usuario)

#Aquí finalizamos el programa
print("FIN DEL PROGRAMA")
        
    

     

    
    
    
    

  






    
    
