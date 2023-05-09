from fpdf import FPDF

def main():
    name = input("Enter your name: ")
    shirtificate_gen(name)

def shirtificate_gen(name):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, 'CS50 Shirtificate', 0, 1, 'C')
    pdf.set_font('Arial', '', 18)

    x = (pdf.w - 100) / 2
    pdf.image('shirtificate.png', x, 50, 100)
    pdf.set_text_color(255, 255, 255)
    x = (pdf.w - pdf.get_string_width(name)) / 2
    pdf.text(x, 90, name)
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()