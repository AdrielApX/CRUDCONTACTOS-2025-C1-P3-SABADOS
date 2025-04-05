#importo json y conecto el archivo json
import json

CONTACTOS_FILE = 'contactos.json'

#cargar contactos
def cargar_contactos():
    try:
        with open(CONTACTOS_FILE, 'r') as archivo:
            contenido = archivo.read()
            if not contenido.strip():  #mensaje por si está vacío
                return []
            return json.loads(contenido)
    except FileNotFoundError:
        return []

def guardar_contactos(contactos): #guardar contactos
    with open(CONTACTOS_FILE, 'w') as archivo:
        json.dump(contactos, archivo, indent=4)

def crear_contacto(nombre, telefono, email):#crear contactos, con las funciones de agregar nombre, numero de telefono y email
    contactos = cargar_contactos()
    nuevo = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(nuevo)
    guardar_contactos(contactos)

def listar_contactos():
    contactos = cargar_contactos()
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}")

def eliminar_contacto(indice):
    contactos = cargar_contactos()
    if 0 <= indice < len(contactos):
        contactos.pop(indice)
        guardar_contactos(contactos)

def editar_contacto(indice, nombre, telefono, email):
    contactos = cargar_contactos()
    if 0 <= indice < len(contactos):
        contactos[indice] = {"nombre": nombre, "telefono": telefono, "email": email}
        guardar_contactos(contactos)
