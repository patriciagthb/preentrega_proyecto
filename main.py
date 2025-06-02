
lista_productos =[]

while True:

  print("Menu de Opciones:")
  print("(1) . Agregar productos")
  print("(2) . Mostrar productos")
  print("(3) . Buscar productos")
  print("(4) . Eliminar productos")
  print("(5) . Salir")

  opcion = input("Seleccione una opcion: ").strip()
  if opcion.isdigit():
    opcion = int(opcion)
  else:
    print("Entrada inválida, por favor ingrese un número") 
    continue

  match opcion:
    case 1: 
      while True:
        while True:
          nombre_producto = input("Ingrese el nombre del producto: ").strip().lower()
          if nombre_producto == "":
            print("El nombre del producto no puede estar vacío.")
          else:
            break

        while True:
          categoria_producto = input("Ingrese la categoría del producto: ").strip().lower()
          if categoria_producto == "":
            print("La categoría del producto no puede estar vacía.")
          else:
            break

        while True:
          precio_producto = input("Ingrese el precio del producto: ").strip()

          if precio_producto == "":
            print("El precio del producto no puede estar vacío.")
            continue
          if precio_producto.isdigit():
            precio_producto = int(precio_producto)
          else:
            print("El precio del producto deber ser un número entero(sin decimales) y no puede ser negativo.")
            continue

          break



        lista_productos.append([nombre_producto, categoria_producto, precio_producto])
        print(f"Se ha agregado el producto '{nombre_producto.capitalize()}' en la categoria '{categoria_producto.capitalize()}' con el precio $ {precio_producto}")

        
        while True:
          respuesta = input("Desea agregar otro producto? s / n : ").strip().lower()

          if respuesta == "n":
           break
          elif respuesta == "s":
            break
          else:
            print("Respuesta inválida. Por favor ingrese s / n : ")
        if respuesta == "n":
            break

    case 2:
      if len(lista_productos) == 0:
        print("No hay productos en la lista.")
      else:
        lista_productos.sort()
        for indice in range(len(lista_productos)):
          print(f"{indice+1}. \t{lista_productos[indice][0]}\t{lista_productos[indice][1]}\t{lista_productos[indice][2]}")

    case 3:
      producto_buscado = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
      productos_encontrados = []

      for producto in lista_productos:
        if producto[0] == producto_buscado:
          productos_encontrados.append(producto)

      if productos_encontrados:
        print(f"Se han encontrado los siguientes productos: {productos_encontrados}\n")

      else:
        print(f"El producto buscado no se encuentra en la lista\n")

    
    case 4:
      if len(lista_productos) == 0:
        print("No hay productos en la lista")

      else:
        lista_productos.sort()
        for indice in range(len(lista_productos)):
          print(f"{indice+1}. \t{lista_productos[indice][0]}\t{lista_productos[indice][1]}\t{lista_productos[indice][2]}")

        while True:

          producto_a_eliminar = input("Ingrese el número de orden en el que se encuentra el producto a eliminar(0 para salir): ").strip()
          if producto_a_eliminar == "0":
            print("Volviendo al menu. ")
            break

          if producto_a_eliminar.isdigit():
            producto_a_eliminar = int(producto_a_eliminar)

            if len(lista_productos) < producto_a_eliminar:
              print("La opcion ingresada no existe ")
              break

            else:
              print(f"Se ha eliminado el producto '{lista_productos[producto_a_eliminar -1][0].capitalize()}'")
              del lista_productos[producto_a_eliminar -1]
              break                         



    case 5:
      print("Hasta pronto!")
      break

    case _n:
      print("La opcion ingresada no es válida (Ingrese un número desde el nro 1 al nro 5)")


