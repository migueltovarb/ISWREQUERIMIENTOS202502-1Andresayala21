contactos = []

print("PROGRAMA DE CONTACTOS ")

while True:
    print("\n1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        cargo = input("Cargo: ")

        # validar si el correo esta repetido

        repetido = False
        for c in contactos:
            if c["correo"] == correo:
                repetido = True
                break

        if repetido:
            print("Ese correo ya existe, prueba con otro.")
        else:
            nuevo = {"nombre": nombre, "telefono": telefono, "correo": correo, "cargo": cargo}
            contactos.append(nuevo)
            print("Contacto guardado correctamente!")

    elif opcion == "2":
        dato = input("Buscar por nombre o correo: ")
        encontrados = []
        for c in contactos:
            if dato in c["nombre"] or dato in c["correo"]:
                encontrados.append(c)

        if encontrados:
            print("\nContactos encontrados:")
            for c in encontrados:
                print(f"{c['nombre']} | {c['telefono']} | {c['correo']} | {c['cargo']}")
        else:
            print("No se encontró ningún contacto.")

    elif opcion == "3":
        if len(contactos) == 0:
            print("No hay contactos aún.")
        else:
            print("\nLista de contactos:")
            for c in contactos:
                print(f"{c['nombre']} | {c['telefono']} | {c['correo']} | {c['cargo']}")

    elif opcion == "4":
        correo = input("Correo del contacto a eliminar: ")
        encontrado = False
        for c in contactos:
            if c["correo"] == correo:
                contactos.remove(c)
                encontrado = True
                print("Contacto eliminado.")
                break

        if not encontrado:
            print("No se encontró ese contacto.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida, intenta otra vez.")
