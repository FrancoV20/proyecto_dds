from app.models.alumno import Alumno
from app.repositories.session import get_session

def agregar_alumno(alumno):
    session = get_session()
    session.merge(alumno)  # Usar merge para insertar o actualizar
    session.commit()
    session.close()

def obtener_alumno_por_legajo(legajo):
    session = get_session()
    result = session.query(Alumno).filter_by(nro_legajo=legajo).first()
    session.close()
    return result

def obtener_alumno_por_nro_documento(nro_documento):
    session = get_session()
    result = session.query(Alumno).filter_by(nro_documento=nro_documento).first()
    session.close()
    return result
