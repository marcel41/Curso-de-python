# Leer de los archivos
# Esta funcion abre el archivo con los estudiantes y regresa una list de strings
def leer_informacion_estudiantes():
    nombre_archivo_datos = 'estudiantes.txt'
    lista_estudiantes = []
    # Open file
    with open(nombre_archivo_datos) as file:
        lineas = file.readlines()
        for linea in lineas:
            atributos_estudiante = linea.split(', ')
            # Eliminar character de nueva linea
            atributos_estudiante[-1] = atributos_estudiante[-1][:-1]
            lista_estudiantes.append(atributos_estudiante)
    return lista_estudiantes

class Estudiante:
    __estudiantes = []
    def __init__(self, id, nombre, apellido, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__id = id
        self.__calificaciones = []
        # Estudiante.estudiantes[id] = self
        Estudiante.__estudiantes.append(self)

    def anadir_calificacion(self, calificacion):
        self.__calificaciones.append(calificacion)

    def __str__(self):
        aprueba_str = 'Aprueba' if self.aprueba() else 'No aprueba'
        return str(self.__id).ljust(5) + self.__nombre.ljust(15) + self.__apellido.ljust(15) \
                + self.__correo.ljust(30) + "{:10.4f}".format(self.promedio()).ljust(15) + aprueba_str.ljust(15)
                # + self.__correo.ljust(30) + str(self.promedio()).ljust(15) + aprueba_str.ljust(15)

    def promedio(self):
        return sum(self.__calificaciones) / len(self.__calificaciones)

    def __lt__(self, other):
        # self.promedio()
        return self.promedio() < other.promedio()

    def aprueba(self):
        return self.promedio() > 7.0

    @staticmethod
    def estudiantes():
        return Estudiante.__estudiantes

datos_estudiantes = leer_informacion_estudiantes()
# estudiantes = []
for datos_estudiante in datos_estudiantes:
    id = int(datos_estudiante[0])
    nombre = datos_estudiante[1]
    apellido = datos_estudiante[2]
    correo = datos_estudiante[3]
    calificaciones = datos_estudiante[4:]
    nuevo_estudiante = Estudiante(id, nombre, apellido, correo)
    for calificacion in calificaciones:
        nuevo_estudiante.anadir_calificacion(float(calificacion))


print('*' * 100)
print('ID'.ljust(5) + 'Nombre'.ljust(15) + 'Apellido'.ljust(15) \
        + 'Correo electronico'.ljust(30) + 'Promedio'.ljust(15) + 'Resultado'.ljust(15))

print('*' * 100)
# estudiantes_ordenados = sorted(Estudiante.estudiantes, reverse=True)
estudiantes_ordenados = sorted(Estudiante.estudiantes(), reverse=True)
for estudiante in estudiantes_ordenados:
    print(estudiante)
