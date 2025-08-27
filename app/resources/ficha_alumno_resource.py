from flask import Blueprint, request, jsonify, send_file
from app.repositories.alumno_repositorio import AlumnoRepositorio
from app.repositories.facultad_repositorio import FacultadRepositorio
from app.services.ficha_alumno_service import FichaAlumnoService
from app.serializers.ficha_alumno_json import ficha_alumno_to_json
from app.serializers.ficha_alumno_pdf import FichaAlumnoPDF
import os

ficha_bp = Blueprint('ficha_alumno', __name__)

@ficha_bp.route('/alumno/<int:alumno_id>/ficha', methods=['GET'])
def ficha_alumno(alumno_id):
    formato = request.args.get('formato', 'json')
    alumno_repo = AlumnoRepositorio()
    facultad_repo = FacultadRepositorio()
    service = FichaAlumnoService(alumno_repo, facultad_repo)
    ficha = service.obtener_ficha(alumno_id)
    if not ficha:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    if formato == 'pdf':
        pdf = FichaAlumnoPDF(ficha)
        filename = f"ficha_alumno_{alumno_id}.pdf"
        pdf_path = os.path.join('/tmp', filename)
        pdf.generar_pdf(pdf_path)
        return send_file(pdf_path, as_attachment=True)
    else:
        return ficha, 200
