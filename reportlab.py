"""
生成PDF檔1
"""
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table,PageBreak,Paragraph,Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pandas as pd

def df_2_pdf(df, fp_pdf):

    # Create a PDF document
    pdf_filename = fp_pdf
    doc = SimpleDocTemplate(pdf_filename)

    # Load the "simhei" font
    pdfmetrics.registerFont(TTFont('SIMSUN', r'C:\Windows\Fonts\SIMSUN.ttc'))

    # Convert the DataFrame to a list of lists (table data)
    elements = []
    # table_data = [df.columns] + df.values.tolist()
    styles = getSampleStyleSheet()
    styleN = ParagraphStyle(
        name='CellStyle',
        parent=styles['Normal'],
        fontName='SIMSUN',
        fontSize=12,  # Set the desired font size here for the cells
        leading=12
    )
    bw1 = df.groupby(["工单号","货号"])
    for group in bw1.groups:
        gp = bw1.get_group(group)
        table_data = [gp.columns] + gp.values.tolist()
        # Create a Table object and set its properties
        table = Table(table_data)
        table.setStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 1)),  # Header row text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment
            ('FONTNAME', (0, 0), (-1, -1), 'SIMSUN'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
            ('BACKGROUND', (0, 0), (-1, 0), (0.9, 0.9, 0.9)),  # Header background color
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # 設置網格線
            ('FONTNAME', (0, 1), (-1, -1), 'SIMSUN'),
        ])
        elements.append(table)

        elements.append(Spacer(1, 12))  #添加空白行
        add2 = Paragraph("This is Test 黃芝2", style=styleN)
        elements.append(add2)
        elements.append(PageBreak())    #添加空白頁


    # Build the PDF document
    doc.build(elements)

    print(f"PDF file '{pdf_filename}' has been created with the DataFrame.")

import pandas as pd
df=pd.read_excel(r"D:\xu\Python\QtPDF\bs_file1\test.xlsx")
df_2_pdf(df,"test.pdf")