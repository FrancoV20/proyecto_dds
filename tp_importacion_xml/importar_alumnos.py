import csv
from app.services.alumno_service import crear_o_actualizar_alumno

CSV_PATH = '../alumnos.csv'  # Ajusta la ruta si es necesario

def importar_alumnos():
    with open(CSV_PATH, encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            crear_o_actualizar_alumno(
                int(row['nro_legajo']),
                row['apellido'],
                row['nombre'],
                row['nro_documento'],
                row['tipo_documento'],
                row['fecha_nacimiento'],
                row['sexo'],
                row['fecha_ingreso']
            )
    print('Importación finalizada.')

if __name__ == '__main__':
    importar_alumnos()
