
from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=True, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", "B", size=24)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(0, 12, txt=row['Topic'], ln=True, align='C')
    for i in range(20, 280, 10):
        pdf.line(10, i, 200, i)

    pdf.ln(257)

    # Add a footer
    pdf.set_font("Times", "I", size=8)
    pdf.set_text_color(254, 180, 180)
    pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')

    for i in range(row['Pages']-1):
        pdf.add_page()
        # Add a footer
        pdf.ln(267)
        pdf.set_font("Times", "I", size=8)
        pdf.set_text_color(254, 180, 180)
        pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')
        for i in range(20, 280, 10):
            pdf.line(10, i, 200, i)


pdf.output("topics.pdf")
