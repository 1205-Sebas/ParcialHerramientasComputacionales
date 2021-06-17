"""
Nombres: Sebastián Gómez Valencia & Angie Tatiana Díaz
Códigos: 8963213 & 8932424
Fecha: 17/06/2021
Actividad: Parcial 
"""
"""
Programa para ordenar un producto en la cafeteria, donde se evalua la condición de estudiante o profesor para aplicar el descuento especifico.
Entradas:
- num_cedula: Pide el número de cedula al usuario.
- produc: Ingresar el código del producto, el cual es visible en el diccionario "productos" con el código, nombre y precio.
- cantidad: Cantidad del producto escogido.
- ir_pagar: Pide el valor para saber si ingresar a pagar.
- prof_est: Determina si es estudiante o profesor, para aplicar el descuento correspondiente.

Salida:
- num_cedula: Imprime en el mensaje de salida el número de cedula para asociar al usuario con la orden.
- valora: En caso de ser estudiante guarda el valor del la multiplicación del valor del producto por su cantidad y despues se hace el desceunto del 50%.
- valorb: En caso de ser profesor guarda el valor del la multiplicación del valor del producto por su cantidad y despues se hace el desceunto del 20%.
- produc: Imprime el código del producto relacionandp costo y producto.
- productos[i][0]: Imprime el nombre del producto escogido relacionado con su código
"""

productos={"001":["Gaseosa",2500],"002":["Cafe",1500],"003":["Empanada",700,]}#Creacion de productos, códigos y precios asociados por diccionario. Clave: Código- Valor:[Nombre,Precio]

print("Bienvenido a la Cafeteria Pan-Huevito y más") #Bienvenida

num_cedula=int(input("Por favor ingrese su número de cedula sin puntos ni comas: ")) #Ingreso cedula
print("Productos:",productos) 

produc=input("Ingrese el código del producto: ")
cantidad=int(input("Ingrese la cantidad del producto: "))

for i in productos: #Reccorer las claves del diccionario
    
    if produc==i:#Comprobar si el código ingresado está en el diccionario de productos.
        valor=(productos[i][1]*cantidad)
        ir_pagar=input("A) Ir a pagar: ")
        
        if ir_pagar=="A" or ir_pagar=="a":
            prof_est=int(input("Usted es\n1) Estudiante\n2) Profesor\n"))#Estudiante o Profesor
            
            if prof_est==1:
                valora = valor * 0.50
                print("El estudiante con cedula",num_cedula,"debe pagar $",valora,"por el producto con codigo",produc,"-",productos[i][0])#Impresón estudiante
            else:
                valorb = valor * 0.80
                print("El profesor con cedula",num_cedula,"debe pagar $",valorb,"por el producto con codigo",produc,"-",productos[i][0])#Impresón profesor
