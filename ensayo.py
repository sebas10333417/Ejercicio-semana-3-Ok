viaje = {}
contador = 0
def seleccionar_destino ():
    while True:
        tipo_vuelo = int(input("""
        ==============================
        ==============================
        1. Internacional
        2. Nacional
        ==============================
        ==============================
        Selecciona una opcion en numero \n
        """))

        if tipo_vuelo == 1: 
            print("="*30)
            print("!!! Viaje Internacional disponible !!! \n Medellin - España \n")
            print("!!! Fecha -> Septiembre 26 !!!: \n  Hora -> 17:50 Hrs")
            categoria = ("!!! Viaje Internacional disponible !!! \n Medellin - España \n")
            fecha = ("!!! Fecha -> Septiembre 26 !!!: \n  Hora -> 17:50 Hrs ")
            usuario = input("Quieres resevar este viaje? / si/no \n ")
            if usuario == "si":
                print("Tu viaje fue reservado con exito")
                vuelo = {
                        "Categoria" : categoria,
                        "Intinerario" : fecha
                        }
                for i , n in vuelo.items():
                    print(i,n)
                break
            else:
                print("="*30)
                continue
        
        elif tipo_vuelo == 2:
            print("="*30)
            print("!!! Viaje nacional disponible !!!  \n Medellin - Bogota")
            print("!!! Fecha -> Octubre 29 !!! \n Hora -> 20:00 Hrs")
            categoria1 = ("!!! Viaje nacional disponible !!!  \n Medellin - Bogota ")
            fecha2 = ("!!! Fecha -> Octubre 29 !!! \n Hora -> 20:00 Hrs ")
            usuario2 = input("Quieres reservar este viaje? / si/no \n")
            if usuario2 == "si":
                print("Tu viaje fue reservado con exito")
                print("="*30)
                vuelo2 = { 
                          "Categoria": categoria1,
                          "Intinerario" : fecha2}
                
                for i, n in vuelo2.items():
                    print(vuelo2)
                break
            else:
                print("="*30)
                continue
            
    return vuelo, vuelo2
                
            
def capacidad_viaje ():
    while True:
        carga = int(input("""
        !!Opciones de quipaje!! \n
        1. Equipaje de mano 
        2. Equipaje de bodega \n
        * Selecciona una opcion *
        
        """))
        
        if carga == 1:
            print("Equipaje de mano seleccionado, peso maximo 10kg: ")
            usuario3 = float(input("Ingresa el peso de tu equipaje \n "))
            if usuario3 > 13:
                print("Peso no aceptado")
            else:
                print("Peso admitidido \n valor -> 120.000 $")
                break
        elif carga == 2:
            print("Equipaje de bodega seleccionado, peso maximo 50 kg")
            usuario4 = int(input("Ingresa el peso de tu equipaje \n "))
            if usuario4 > 50:
                print("Peso no aceptado")
                continue
            else:
                print("Peso admitidido \n valor -> 270.000 $")
                break

def comprar_boleto(viaje):
    
    while True:
        
        print("Por favor ingresa los siguientes datos \n ")
        num_id = int(input("Por favor ingresa tu numero de identificacion -> : \n"))
        comprador = input("Por favor ingresa tu nombre -> : \n")
        apellido = input("Por favor ingresa tu apellido -> :\n")
        
        viaje[num_id] = {
            "Comprador" : comprador,
            "Apellido" : apellido
            }
        
        for i, n in viaje.items():
            print(i , n)
            break
        seguir_comprando = input("quiere comprar otro boleto? (si/no)")
        if seguir_comprando == "si":
            print("")
        elif seguir_comprando == "no":
            break
    return viaje
