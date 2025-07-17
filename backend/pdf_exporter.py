from fpdf import FPDF   

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0,10, "Podcast Summary Report", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, text):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, text)
        self.ln(5)

def generate_pdf(summary, chapters, transcript, output_path):
    pdf=PDFReport()
    pdf.add_page()

    pdf.section_title("Summary")
    pdf.section_body(summary)

    pdf.section_title("Chapters")
    for chapter in chapters:
        pdf.section_body(f"{chapter}")
    
    pdf.section_title("Transcript")
    pdf.section_body(transcript)

    pdf.output(output_path)
