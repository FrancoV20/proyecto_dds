from app.models.alumno import Alumno
from app.models.facultad import Facultad

class FichaAlumnoService:
    def __init__(self, alumno_repo, facultad_repo):
        self.alumno_repo = alumno_repo
        self.facultad_repo = facultad_repo

    def obtener_ficha(self, alumno_id):
        alumno = self.alumno_repo.obtener_por_id(alumno_id)
        if not alumno:
            return None
        facultad = self.facultad_repo.obtener_por_id(alumno.facultad_id)
        return {
            'legajo': alumno.legajo,
            'apellido': alumno.apellido,
            'nombre': alumno.nombre,
            'facultad': facultad.nombre if facultad else None
        }
