class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        return f'Estudiante: {self.nombre} - ID: {self.id_estudiante} - Cursos: {[curso.nombre for curso in self.cursos]}'

class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.est
