#importe el archivo contactos.py
import contactos

def menu():#cree un menu con las deiferentes opciones de un contacto
    while True:
        print("\n==== AGENDA DE CONTACTOS ====")
        print("1. Ver contactos")
        print("2. Añadir contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            contactos.listar_contactos()
        elif opcion == "2":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            contactos.crear_contacto(nombre, telefono, email)
        elif opcion == "3":
            contactos.listar_contactos()
            i = int(input("Número de contacto a editar: ")) - 1
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            contactos.editar_contacto(i, nombre, telefono, email)
        elif opcion == "4":
            contactos.listar_contactos()
            i = int(input("Número de contacto a eliminar: ")) - 1
            contactos.eliminar_contacto(i)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
