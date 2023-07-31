from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from pybraille import convert_text_to_braille

def create_braille_pdf(text, file_name):
    braille_text = convert_text_to_braille(text)
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()
    story = [Paragraph(braille_text, styles["Normal"])]
    doc.build(story)

if __name__ == "__main__":
    brallie_text = "This is the brallie text that you want to save as a PDF in Braille."
    file_name = "braille_document.pdf"
    create_braille_pdf(brallie_text, file_name)
