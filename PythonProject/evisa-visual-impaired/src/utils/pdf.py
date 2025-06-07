def create_visa_application_pdf(firstname, lastname, address, gender, img_path):
    from fpdf import FPDF
    import os

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, "E-Visa Application Form", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(50, 10, f"First Name: {firstname}", ln=True)
    pdf.cell(50, 10, f"Last Name: {lastname}", ln=True)
    pdf.cell(50, 10, f"Gender: {gender}", ln=True)
    pdf.multi_cell(0, 10, f"Address: {address}", align="L")
    pdf.ln(10)
    pdf.cell(50, 10, "Applicant Photo:", ln=True)
    if os.path.exists(img_path):
        pdf.image(img_path, x=pdf.get_x(), y=pdf.get_y(), w=40)
    pdf_path = "visa_application.pdf"
    pdf.output(pdf_path)
    return pdf_path