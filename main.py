'''Programa de inventario de productos - Universidad Popular del Cesar seccional Aguachica
@Autor -> Didier Fernando Guerrero Sumalave
programación 1
15 de marzo del 2023
'''

#Importaciones 


#Definición de la data
data_products = []
data_clients = []
data_ventas = []
users_admin = ["dfguerrero", 12345]
users_ventas = ["ventas1", 12345]

#Funciones generales del programa

def validar_usuario(admin_lista:list, ventas_lista:list):
    #Función que valida que rol esta iniciando sesión.
    admin = False
    ventas = False
    user = input("Digite su usuario: ")
    password = int(input("Digite su contraseña: "))
    if user in admin_lista:
        if password == admin_lista[1]:
            admin = True
            return admin, 1
        else:
            return admin, 1
    elif user in ventas_lista:
        if password == ventas_lista[1]:
            ventas = True
            return ventas, 2
        else:
            return ventas, 2
    return False, 0

def menu_administrador():
    while(True):
        print("*****Menu del administrador*****")
        print("")
        print("SUPERMERCADO TIENDITA UPC")
        print("")
        print("1. Agregar productos al inventario")
        print("2. Buscar productos en el inventario")
        print("3. Editar productos en el inventario")
        print("4. Eliminar un producto")
        print("5. Agregar clientes ")
        print("6. Buscar un cliente")
        print("7. Editar los datos de un cliente")
        print("8. Eliminar un cliente")
        print("9. Realizar una venta")
        print("10. Buscar una venta")
        print("11. Editar una venta")
        print("12. Eliminar una venta")
        print("13. Reporte de ventas")
        print("14. Inicializar la caja/Cerrar la caja")
        print("15. Salir del programa")
        opcion = int(input("Digite una opción: "))
        if opcion == 1:
            x = add_products(data_products)
            print(x)
            continue
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            pass
        elif opcion == 11:
            pass
        elif opcion == 12:
            pass
        elif opcion == 13:
            pass
        elif opcion == 14:
            pass
        elif opcion == 15:
            pass
        else:
            print("¡La opción no es correcta!")

def menu_cajero():
    print("*****Menu del cajero*****")
    print("")
    print("SUPERMERCADO TIENDITA UPC")
    print("1. Modulo de ventas")
    print("2. Salir")
    opcion = int(input("Digite una opción: "))
    if opcion == 1:
        print("")
        print("****Modulo de ventas****")

    elif opcion == 2:
        print ("Usted esta saliendo del modulo de ventas")
        return
    
def add_products(data_products):
    data_product = []
    print("Modulo para agregar productos")
    codigo = int(input("Digite el codigo del producto: "))
    #Crear una función que valide que no se repitan productos, clientes y ventas.
    nombre = input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio del producto: "))
    cant_inventario = float(input("Digite la cantidad de unidades: "))
    data_product.append(codigo)
    data_product.append(nombre)
    data_product.append(precio)
    data_product.append(cant_inventario)
    print(data_product)
    print(data_products)
    data_products.append(data_product)
    return data_products
    
    
if __name__ == "__main__":
    while (True):
        t_usuario, rol = validar_usuario(users_admin, users_ventas)
        if t_usuario == True and rol == 1:
            menu_administrador()
        elif t_usuario == True and rol == 2:
            menu_cajero()
        else:
            print ("Los datos no pudieron ser comprobados")

        