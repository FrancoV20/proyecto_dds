# Trabajo Práctico: Importación de XML (TP1) y Alumnos desde CSV (TP2)

## Descripción
Este proyecto permite importar datos desde archivos XML (TP1) y desde un archivo CSV de alumnos (TP2) a una base de datos PostgreSQL usando SQLAlchemy.

## Requisitos
- Python 3.11+
- PostgreSQL
- Paquetes de Python: ver `requirements.txt`
- (Opcional) Docker y docker-compose

**Importante:** Si usas Docker, asegúrate de que la contraseña, usuario y nombre de base de datos en el `docker-compose.yml` no tengan tildes, ñ ni caracteres especiales. Usa solo letras y números para evitar errores de conexión.

Si necesitas cambiar la contraseña de la base de datos en Docker, edita el archivo `docker-compose.yml` así:

```yaml
environment:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: tu_contraseña_simple
  POSTGRES_DB: tp1_importacion_xml
```

Luego, actualiza la cadena de conexión en tu código, por ejemplo en `app/repositories/session.py`:

```python
DATABASE_URL = 'postgresql://postgres:tu_contraseña_simple@localhost:5432/tp1_importacion_xml'
```

O en la variable de entorno `DATABASE_URL` si la usas.

## Pasos para ejecutar ambos trabajos prácticos desde cero

### 1. Crear la base de datos
(Ejecutar en psql o tu cliente SQL)
```sql
CREATE DATABASE tp1_importacion_xml;
```

### 2. Levantar la base de datos con Docker (opcional)
```powershell
docker-compose up -d
```

### 3. Instalar dependencias
```powershell
pip install -r requirements.txt
```

### 4. Importar todos los XML (TP1)
```powershell
python importar_todos.py
```
O bien:
```powershell
python main.py
```

### 5. Crear las tablas de alumnos (TP2)
```powershell
python crear_tablas.py
```

### 6. Vaciar la tabla de alumnos (opcional, TP2)
```powershell
python vaciar_alumnos.py
```

### 7. Importar los alumnos desde el CSV (TP2)
```powershell
python importar_alumnos.py
```

### 8. Ejecutar los tests
```powershell
python -m unittest tests/test_importacion.py
```

### 9. (Opcional) Verificar cantidad de registros importados
(Ejecutar en tu cliente SQL)
```sql
SELECT COUNT(*) FROM alumnos;
SELECT COUNT(*) FROM paises;
-- Y así para cada tabla relevante
```

Cualquier duda, consulta el código o los comentarios en cada archivo.
