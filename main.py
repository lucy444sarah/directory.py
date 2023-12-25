import os

CARPETA = 'contactos/'  # carpeta de contactos
EXTENSION = '.txt'  # Extension de archivos

# Contactos


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe
    crear_directorio()

    # Muestra el Menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Selecione una opcion: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones:
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver Contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar Contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar Contacto')
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')

    with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

        # Resto de los campos
        telefono_contacto = input('Agrega el telefono:\r\n')
        categoria_contacto = input('Categoria Contacto:\r\n')

        # Instanciar la classe
        contacto = Contacto(
            nombre_contacto, telefono_contacto, categoria_contacto)

        # Escribir en el archivo
        archivo.write('Nombre: ' + contacto.nombre + '\r\n')
        archivo.write('Telefono: ' + contacto.telefono + '\r\n')
        archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        # Mostrar un mensaje que todo salio OK
        print('\r\n Contacto creado correctamente \r\n')


def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer: ')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')


def crear_directorio():
    if not os.path.exists('CARPETA'):
        # crea la carpeta
        os.makedirs('CARPETA')


app()
