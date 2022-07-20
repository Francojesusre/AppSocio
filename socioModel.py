from fileinput import close
import pyodbc
import pathlib


def OpenConection():
    try:
        conection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server=localhost;"
                                   "Database=AppSocio;"
                                   "Trusted_Connection=yes;")
        # print("La conexión a la base de datos fue correcta")
        return conection
    except (Exception) as err:
        print("Ocurrió el siguiente error en la conexión a la base de datos: ",
              err)


def CloseConection(conection):
    try:
        conection.close()
        # print("La conexión a la base de datos cerrada de forma correcta")
    except (Exception) as err:
        print("Ocurrió el siguiente error al cerrar la conexión a la base de datos: ", err)


def GetById(id: int):
    try:
        query = 'SELECT * FROM socios WHERE id = ? '
        conection = OpenConection()
        cursor = conection.cursor()
        cursor.execute(query, (id))
        return cursor.fetchone()
    except (Exception) as err:
        raise Exception(
            "Ocurrió el siguiente error al querer recuperar los datos del socio: ", err)
    finally:
        CloseConection(conection)


def GetAll():
    query = 'SELECT * FROM socios ORDER BY nombre ASC'
    try:
        conection = OpenConection()
        cursor = conection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except (Exception) as err:
        raise Exception(
            "Ocurrió el siguiente error al querer recuperar todos los socios: ", err)
    finally:
        CloseConection(conection)


def Update(socio):
    if socio.id == 0:
        query = "INSERT INTO socios(nombre,apellido,DNI,email) VALUES (?,?,?,?)"
        values = (socio.nombre, socio.apellido, socio.DNI, socio.email)
    else:
        query = "UPDATE socios SET nombre = ?, apellido = ?, DNI = ?, email = ? where id = ?"
        values = (socio.nombre, socio.apellido,
                  socio.DNI, socio.email, socio.id)
    try:
        conection = OpenConection()
        cursor = conection.cursor()
        cursor.execute(query, values)
        conection.commit()
        print("")
        if socio.id == 0:
            print("Socio registrado con éxito!\n")
        else:
            print("Socio actualizado con éxito!\n")

    except (Exception) as err:
        if socio.id == 0:
            txt = "Ocurrió el siguiente error al querer dar de alta el socio: "
        else:
            txt = "Ocurrió el siguiente error al querer actualizar el socio: "
        raise Exception(txt, err)
    finally:
        CloseConection(conection)


def Delete(id: int):
    query = 'DELETE FROM socios WHERE id = ?'
    try:
        conection = OpenConection()
        cursor = conection.cursor()
        cursor.execute(query, (id))
        conection.commit()
        print("")
        print("Socio eliminado con éxito!\n")
    except (Exception) as err:
        raise Exception(
            "Ocurrió el siguiente error al querer eliminar el socio:", err)
    finally:
        CloseConection(conection)


def ExportData(file_name):
    try:
        socios = GetAll()
        if len(socios) > 0:
            text_file = open(file_name + ".txt", "w")
            for socio in socios:
                datos = "Id: {0} --- Nombre: {1} --- Apellido: {2} --- DNI: {3} --- Email: {4}"
                text_file.write(datos.format(socio[0], socio[1],
                                             socio[2], socio[3], socio[4]))
            text_file.close()
            print("Datos exportados con éxito!")
    except (Exception) as err:
        raise Exception(
            "Ocurrió el siguiente error al exportar los datos: ", err)


def BackupData(file_name):
    try:
        file_path = pathlib.Path(file_name)
        if file_path.exists():
            file1 = open(file_path, 'r')
            file2 = open("C:\Temporales\\" + file_name, 'w')
            file2.write(file1.read())
            print("Archivo copiado con éxito!")
            file1.close()
            file2.close()
        else:
            print("El archivo buscado no existe")
    except (Exception) as err:
        raise Exception(
            "Ocurrió el siguiente error al hacer el backup de los datos: ", err)
