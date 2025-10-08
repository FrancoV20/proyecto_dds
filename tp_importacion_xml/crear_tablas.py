from app.models.base import Base
from app.models.alumno import Alumno  # Importar el modelo para que se registre
from app.repositories.session import engine

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("¡Tablas creadas correctamente!")
