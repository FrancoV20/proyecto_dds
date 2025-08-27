from fpdf import FPDF

class FichaAlumnoPDF:
    def __init__(self, ficha):
        self.ficha = ficha

    def generar_pdf(self, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Ficha del Alumno', ln=True, align='C')
        pdf.ln(10)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f"Legajo: {self.ficha['legajo']}", ln=True)
        pdf.cell(0, 10, f"Apellido: {self.ficha['apellido']}", ln=True)
        pdf.cell(0, 10, f"Nombre: {self.ficha['nombre']}", ln=True)
        pdf.cell(0, 10, f"Facultad: {self.ficha['facultad']}", ln=True)
        pdf.output(filename)
        return filename
