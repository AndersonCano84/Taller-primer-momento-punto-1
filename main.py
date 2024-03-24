import random

productos = []
productos_por_zona = {"A": 0, "B": 0, "C": 0, "D": 0}

def generar_id():
    return random.randint(1, 100)

def total_productos_registrados():
    return sum(productos_por_zona.values())

while True:
    print("\n*** MENÚ ***")
    print("1. Registrar Producto")
    print("2. Mostrar Productos en Bodega")
    print("3. Buscar Producto por Nombre")
    print("4. Modificar Número de Unidades Compradas")
    print("5. Eliminar Producto")
    print("6. Finalizar")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 6:
            raise ValueError("Opción inválida")
        
        if opcion == 1:
            if total_productos_registrados() >= 200:
                print("Error: La cantidad máxima de productos en la tienda ha sido alcanzada.")
                continue
            else:
                while True:
                    try:
                        zona = input("Ubicación en la tienda (A, B, C o D): ").upper()
                        if zona not in productos_por_zona:
                            raise KeyError("Ubicación no válida")
                        if productos_por_zona[zona] >= 50:
                            print(f"Error: Se alcanzó el límite de productos en la zona {zona}.")
                        else:
                            producto = {}
                            producto["id"] = generar_id()
                            producto["nombre"] = input("Nombre del producto: ")
                            producto["precio"] = input("Precio unitario del producto: ")
                            producto["ubicacion"] = zona
                            producto["descripcion"] = input("Descripción del producto: ")
                            producto["casa"] = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
                            producto["referencia"] = input("Referencia (código alfanumérico): ")
                            producto["pais_origen"] = input("País de origen del producto: ")
                            while True:
                                try:
                                    producto["unidades_compradas"] = int(input("Número de unidades compradas del producto: "))
                                    if producto["unidades_compradas"] <= 0:
                                        print("Error: Debe ingresar un número positivo de unidades.")
                                    elif total_productos_registrados() + producto["unidades_compradas"] > 200:
                                        print("Error: La cantidad total de productos excede el límite de 200. Por favor, corrija.")
                                    elif productos_por_zona[zona] + producto["unidades_compradas"] > 50:
                                        print(f"Error: La cantidad de productos en la zona {zona} excede el límite de 50. Por favor, corrija.")
                                    else:
                                        break
                                except ValueError:
                                    print("Error: Debe ingresar un número entero válido para las unidades compradas.")
                            producto["precio"] = int(producto["precio"])  
                            producto["garantia_extendida"] = input("Producto con garantía extendida (true/false): ").lower() == 'true'
                            productos.append(producto)
                            productos_por_zona[zona] += producto["unidades_compradas"]
                            print("Producto registrado correctamente.")
                            break
                    except KeyError:
                        print("Error: Ubicación no válida. Por favor, ingrese una ubicación válida (A, B, C o D).")
                
        elif opcion == 2:
            print("*** Productos en Bodega ***")
            if len(productos) == 0:
                print("No hay productos en bodega.")
            else:
                for producto in productos:
                    print("ID:", producto["id"])
                    print("Nombre:", producto["nombre"])
                    print("Precio:", producto["precio"])
                    print("Descripción:", producto["descripcion"])
                    print()
        
        elif opcion == 3:
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            for producto in productos:
                if producto["nombre"].lower() == nombre_producto.lower():
                    encontrado = True
                    print("ID:", producto["id"])
                    print("Nombre:", producto["nombre"])
                    print("Precio:", producto["precio"])
                    print("Descripción:", producto["descripcion"])
                    break
            if not encontrado:
                print("El producto no se encuentra en el inventario.")
        
        elif opcion == 4:
            nombre_producto = input("Ingrese el nombre del producto a modificar: ")
            encontrado = False
            for producto in productos:
                if producto["nombre"].lower() == nombre_producto.lower():
                    encontrado = True
                    unidades_nuevas = int(input("Ingrese el nuevo número de unidades compradas: "))
                    if unidades_nuevas <= producto["unidades_compradas"]:
                        producto["unidades_compradas"] = unidades_nuevas
                        print("Unidades compradas actualizadas con éxito.")
                    else:
                        print("Error: El número de unidades ingresado es mayor al número inicial.")
                    break
            if not encontrado:
                print("El producto no se encuentra en el inventario.")
        
        elif opcion == 5:
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
            encontrado = False
            for producto in productos:
                if producto["nombre"].lower() == nombre_producto.lower():
                    encontrado = True
                    confirmacion = input(f"¿Está seguro de eliminar '{producto['nombre']}'? (Sí/No): ").lower()
                    if confirmacion == "si":
                        zona = producto["ubicacion"]
                        productos_por_zona[zona] -= 1
                        productos.remove(producto)
                        print("Producto eliminado del inventario.")
                    else:
                        print("Operación cancelada.")
                    break
            if not encontrado:
                print("El producto no se encuentra en el inventario.")
        
        elif opcion == 6:
            print("¡Hasta luego!")
            break  
        
    except ValueError:
        print("Error: Debe ingresar un número entero para seleccionar una opción válida.")
