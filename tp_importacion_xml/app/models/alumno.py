from sqlalchemy import Column, Integer, String
from .base import Base

class Alumno(Base):
    __tablename__ = 'alumnos'
    nro_legajo = Column(Integer, primary_key=True, autoincrement=True)
    apellido = Column(String(50), nullable=False)
    nombre = Column(String(50), nullable=False)
    nro_documento = Column(String(20), nullable=False, unique=True)
    tipo_documento = Column(String(20), nullable=False)
    fecha_nacimiento = Column(String(10), nullable=False)  # 'YYYY-MM-DD'
    sexo = Column(String(1), nullable=False)
    fecha_ingreso = Column(String(10), nullable=False)  # 'YYYY-MM-DD'