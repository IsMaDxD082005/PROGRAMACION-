from proveedores import proveedor
from productos import producto

global prov1, prod1
Opcion = ""
prov1 = proveedor()
prod1 = producto()

while Opcion!=5 :
    print("1. Agregar Proveedor")
    print("2. Crear un Producto")
    print("3. Agregar producto a Proveedor")
    print("4. Listar Productos")
    print("5. Salir")
    print("Ingrese la opcion la desea: ")
    Opcion = int(input())

    if Opcion == 1:
        
        # CAPTURA DE DATOS DESDE TECLADO
        apellidos = input("Ingrese Apellidos:")
        nombre = input("Ingrese Nombre:")
        telefono = input("Ingrese Telefono:")

        #CREAR EL PROVEEDOR
        prov1.AgregarProveedor(apellidos,nombre,telefono)

    elif Opcion == 2:
        

        # PEDIR INGRESO DE DATOS DEL PRODUCTO
        codigo = int(input("Ingrese codigo del producto"))
        nomproducto = input("Ingrese el nombre del producto")
        precio = int(input("Ingrese precio del producto"))
                    
        # CREAR PRODUCTO
        prod1.CrearProducto(codigo,nomproducto,precio)

    elif Opcion == 3:
        prov1.AgregarProductos(prod1)

    elif Opcion ==4:
        prod1.ListaProductos(prod1)