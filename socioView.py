import socioController
import os


def screen_clear():
    _ = os.system('cls')


def menu_principal():
    item = 0
    while item != 99:
        screen_clear()
        print('')
        print('##################')
        print('### MENU SOCIOS ###')
        print('##################')
        print('')
        print('Menú de opciones:')
        print('-----------------')
        print('')
        print(' 1 - Buscar socio')
        print(' 2 - Alta nuevo socio')
        print(' 3 - Modificacion socio')
        print(' 4 - Baja socio')
        print(' 5 - Listar socios')
        print(' 6 - Exportar socios')
        print(' 7 - Backup data')
        print('99 - Finalizar')
        print('')
        item = int(
            input('Ingrese la opción deseada y presione ENTER para continuar:\n'))

        if item == 1:
            id = ingresar_id_socio_search()
            socio = socioController.GetById(id)
            if socio:
                mostrar_socio(socio)
            else:
                print('### Búsqueda sin resultados. El Id de Socio:',
                      id, 'no existe ###')
                input('Presione ENTER para continuar.\n')
            continue
        elif item == 2:
            socioNuevo = newSocio()
            socioController.Update(socioNuevo)
            input('Presione ENTER para continuar.\n')
            continue
        elif item == 3:
            id = ingresar_id_socio_mod()
            socioMod = modSocio(id)
            socioController.Update(socioMod)
            input('Presione ENTER para continuar.\n')
            continue
        elif item == 4:
            id = ingresar_id_socio_del()
            socioController.Delete(id)
            input('Presione ENTER para continuar.\n')
            continue
        elif item == 5:
            listarSocios()
            input('Presione ENTER para continuar.\n')
            continue
        elif item == 6:
            name = nombre_archivo()
            socioController.ExportData(name)
            input('Presione ENTER para continuar.\n')
            continue
        elif item == 7:
            name = nombre_archivo()
            socioController.BackupData(name)
            input('Presione ENTER para continuar.\n')
            continue
        elif item != 99:
            input('La opción ingresada no es válida, presione ENTER para continuar.\n')


def ingresar_id_socio_search():
    screen_clear()
    print('')
    print('########################################################')
    print('### Ingrese Id del socio a buscar')
    print('########################################################')
    print('--------------------------------------------------------')
    id = input('Id Socio: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return id


def ingresar_id_socio_mod():
    screen_clear()
    listarSocios()
    print('')
    print('########################################################')
    print('### Ingrese Id del socio a modificar')
    print('########################################################')
    print('--------------------------------------------------------')
    id = input('Id Socio: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return id


def ingresar_id_socio_del():
    screen_clear()
    listarSocios()
    print('')
    print('########################################################')
    print('### Ingrese Id del socio a eliminar')
    print('########################################################')
    print('--------------------------------------------------------')
    id = input('Id Socio: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return id


def nombre_archivo():
    screen_clear()
    listarSocios()
    print('')
    print('########################################################')
    print('### Ingrese el nombre del archivo')
    print('########################################################')
    print('--------------------------------------------------------')
    name = input('Nombre: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return name


def mostrar_socio(socio):
    screen_clear()
    print('')
    print('########################################################')
    print('### DATOS SOCIO ID: {}'.format(socio.id))
    print('########################################################')
    print('--------------------------------------------------------')
    print('Nombre: {}'.format(socio.nombre))
    print('--------------------------------------------------------')
    print('Apellido: {}'.format(socio.apellido))
    print('--------------------------------------------------------')
    print('DNI: {}'.format(socio.DNI))
    print('--------------------------------------------------------')
    print('Email: {}'.format(socio.email))

    print('')
    input('Presione ENTER para continuar.\n')


def listarSocios():
    socios = socioController.GetAll()
    print('')
    print('Socios:')
    print('')
    for socio in socios:
        datos = "Id: {0} --- Nombre: {1} --- Apellido: {2} --- DNI: {3} --- Email: {4}"
        print(datos.format(socio[0], socio[1],
              socio[2], socio[3], socio[4]))
    print('')


def newSocio():
    screen_clear()
    print('')
    print('########################################################')
    print('### Ingrese los datos del nuevo socio ###',)
    print('########################################################')
    print('--------------------------------------------------------')
    nombre = input('Nombre: ')
    print('--------------------------------------------------------')
    apellido = input('Apellido: ')
    print('--------------------------------------------------------')
    dni = input('DNI: ')
    print('--------------------------------------------------------')
    email = input('Email: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return socioController.Socio(0, nombre, apellido, dni, email)


def modSocio(id):
    print('')
    print('########################################################')
    print('### Ingrese los nuevos datos del nuevo socio ###',)
    print('########################################################')
    print('--------------------------------------------------------')
    nombre = input('Nombre: ')
    print('--------------------------------------------------------')
    apellido = input('Apellido: ')
    print('--------------------------------------------------------')
    dni = input('DNI: ')
    print('--------------------------------------------------------')
    email = input('Email: ')
    print('--------------------------------------------------------')
    print('')
    input('Presione ENTER para continuar.\n')
    return socioController.Socio(id, nombre, apellido, dni, email)


# ------------------------------------------------------------------------------------------------------------------------------
# https://github.com/mkleehammer/pyodbc/issues/998#issuecomment-1035368786
# python -W ignore::DeprecationWarning socioView.py
menu_principal()
