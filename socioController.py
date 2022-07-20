import socioModel


def GetById(id):
    try:
        row = socioModel.GetById(id)
        # if row is not None:
        return Socio(row[0], row[1], row[2], row[3], row[4])
    except (Exception) as err:
        print(err)


def GetAll():
    try:
        rows = socioModel.GetAll()
        return rows
    except (Exception) as err:
        print(err)


def Update(socio):
    try:
        socioModel.Update(socio)
    except (Exception) as err:
        print(err)


def Delete(id):
    try:
        socioModel.Delete(id)
    except (Exception) as err:
        print(err)


def ExportData(file_name):
    try:
        socioModel.ExportData(file_name)
    except (Exception) as err:
        print(err)


def BackupData(file_name):
    try:
        socioModel.BackupData(file_name)
    except (Exception) as err:
        print(err)


class Socio:
    def __init__(self, id, nombre, apellido, DNI, email):
        self.id = int(id)
        self.apellido = apellido
        self.nombre = nombre
        self.DNI = DNI
        self.email = email
