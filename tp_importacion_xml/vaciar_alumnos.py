from app.repositories.session import get_session
from sqlalchemy import text

if __name__ == "__main__":
    session = get_session()
    session.execute(text("DELETE FROM alumnos;"))
    session.commit()
    session.close()
    print("Tabla alumnos vaciada.")
