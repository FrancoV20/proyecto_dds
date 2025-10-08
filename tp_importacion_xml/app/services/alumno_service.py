from app.models.alumno import Alumno
from app.repositories.alumno_repositorio import agregar_alumno, obtener_alumno_por_nro_documento

def crear_o_actualizar_alumno(nro_legajo, apellido, nombre, nro_documento, tipo_documento, fecha_nacimiento, sexo, fecha_ingreso):
    alumno = obtener_alumno_por_nro_documento(nro_documento)
    if not alumno:
        alumno = Alumno(
            nro_legajo=nro_legajo,
            apellido=apellido,
            nombre=nombre,
            nro_documento=nro_documento,
            tipo_documento=tipo_documento,
            fecha_nacimiento=fecha_nacimiento,
            sexo=sexo,
            fecha_ingreso=fecha_ingreso
        )
    else:
        alumno.nro_legajo = nro_legajo
        alumno.apellido = apellido
        alumno.nombre = nombre
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = fecha_nacimiento
        alumno.sexo = sexo
        alumno.fecha_ingreso = fecha_ingreso
    agregar_alumno(alumno)
    return alumno

