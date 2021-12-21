from fpdf import FPDF

async def write(number):

    with open(f'reports_rsa/{number.upper()}.txt', 'r') as file:
        line = file.readlines()
        lst = []
        lst_gen = []
        for i in line:
            lst.append(i.strip('\n'))
            if i == '\n':
                lst_gen.append(lst)
                lst = []
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'font/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)
    for i in lst_gen:
        for j in i:
            pdf.cell(200, 10, txt=j, ln=1, align='C')
    pdf.output(f'reports_rsa_pdf/{number.upper()}.pdf')