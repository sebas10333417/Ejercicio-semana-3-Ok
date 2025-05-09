lista = {}

continuar = True

while continuar:
    print("!!! BIENVENIDO AL MENU !!!")
    lista_menu = int(input("""
    1. Añadir productos
    2. Consultar productos
    3. Actualizar precios
    4. Eliminar productos
    5. Calcular valor total del inventario \n
    --------------------
    --------------------
    Por favor ingresa una opcion
    --------------------
    --------------------
    """))

    if lista_menu == 1:
        id = int(input("Por favor ingresa el ID del producto -> : \n"))
        producto = input("Por favor ingresa el nombre del producto -> : \n")
        precio = int(input("Por favor ingresa el valor del producto -> : \n"))
        cantidad = int(input("Por favor ingresa la cantidad a registrar -> : \n "))

        lista[id] = {
            "Nombre producto" : producto,
            "Precio producto" : precio,
            "Cantidad disponible" : cantidad
        }

        for i , n in lista.items():
            print(i , n )

    elif lista_menu == 2:
        consultar = int(input("Ingresa el ID del producto que quieres consultar -> : \n"))
        if not consultar in lista:
            print("El ID del producto no se encuentra registrado. ")

        else:
            info_producto = lista.get(consultar)
            print(f"{consultar} {info_producto}")

    elif lista_menu == 3:
        actualizar = int(input("Por favor ingresa el ID del producto que deseas actualizar -> : \n "))
        precio_nuevo = int(input("Por favor ingresa el nuevo valor -> : \n"))
        lista[actualizar]["Precio producto"] = precio_nuevo
        print(lista)

    elif lista_menu == 4:
        el  = int(input("Ingresa el ID del producto que deseas eliminar -> : \n"))
        del lista[el]
        print("El producto fue eliminado con exito ")
        print(lista)

    elif lista_menu == 5:
        total = 0
        
        for u , m in lista.items():
            cantidad_sub = m.get("Cantidad disponible")
            precio_sub = m.get("Precio producto")
            sub_total = (cantidad_sub * precio_sub)
            total = total + sub_total 
        print("El total del inventario es -> :")
        print(total)