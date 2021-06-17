# Parcial Herramientas Computacionales
Parcial Herramientas Computacionales - Sebastián Gómez &amp; Angie Tatiana Díaz
### Problema Parcial 
Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor,tienen descuentos diferentes. Se desea saber entonces por cada compra cuánto debe pagar el
usuario en caja. 
Para ello:
* Pida por teclado la siguiente información para el cliente: cédula y rol: profesor o estudiante
* Registrar el producto a comprar: codigo producto, cantidad de unidades y precio del producto. (un solo producto, varias unidades, por ejemplo: producto 076: gaseosa, 3 unidades)
* Los descuentos estan dados de la siguiente forma: los estudiantes tienen un 50 % de descuento mientras que los profesores tienen un 20 % de descuento
Al final el procedimiento por cada cliente deber´a imprimir el valor a pagar por sus productos
de la forma: ”El Rol con cedula Numero, debe pagar Valor por el producto Codigo.


**Ejemplo: ”El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076”.**


Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la
cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cédula de cada cliente
y el código del producto llevado en el mensaje.
### Explicación Problema (Resolución- Entradas - Salidas)

**Explicación:** Programa para ordenar un producto en la cafeteria, donde se evalua la condición de estudiante o profesor para aplicar el descuento especifico.

***Entradas:***
- num_cedula: *Pide el número de cedula al usuario.*
- produc: *Ingresar el código del producto, el cual es visible en el diccionario "productos" con el código, nombre y precio.*
- cantidad: *Cantidad del producto escogido.*
- ir_pagar: *Pide el valor para saber si ingresar a pagar.*
- prof_est: *Determina si es estudiante o profesor, para aplicar el descuento correspondiente.*

***Salida:***
- num_cedula: *Imprime en el mensaje de salida el número de cedula para asociar al usuario con la orden.*
- valora: *En caso de ser estudiante guarda el valor del la multiplicación del valor del producto por su cantidad y despues se hace el descuento del 50%.*
- valorb: *En caso de ser profesor guarda el valor del la multiplicación del valor del producto por su cantidad y despues se hace el descuento del 20%.*
- produc: *Imprime el código del producto relacionandp costo y producto.*
- productos[i][0]: *Imprime el nombre del producto escogido relacionado con su código*

**Ubicación resultado**: *parcialHerramienta.py*

En el archivo **punto2_parcialherramientas** se encuentra la respuesta a las preguntas realizadas en el punto 2 de la consigna.

1. **¿Qué tipo de errores se presentaron o se pueden presentar con su implementación al
problema?**


Los tipos de errores que podrían presentarse serían;
 - Errores de sintaxis: Los errores de sintaxis podrían presentarse con el manejo de los
			condicionales, siguiendo un orden correcto y así asegurar un buen funcionamiento.
 - Errores de ejecución: El usuario podría ingresar valores alfabeticos donde deberían ir valores
			 valores númericos y viceversa.
2. **¿Qué estrategias podría usar para solucionar estos errores?**


Las estrategias que utilizaremos seran, el uso de "fuerza bruta" así como la estrategía de vuelta atras,
para garantizar un buen funcionamiento logico, adicionalmente, se pondran instrucciones especificas en 
las impresiones por consola para que el usuario ingrese los valores correctos. 

Estrategias a utilizar:
- Fuerza bruta
- Vuelta atras

