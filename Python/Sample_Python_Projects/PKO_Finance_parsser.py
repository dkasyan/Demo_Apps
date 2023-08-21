import csv
import re
import pdfreader
import PyPDF2

from pdfreader import PDFDocument, SimplePDFViewer


data = []
input_csv = 'lista_operacji_230401_230419_202304191524525552.csv'


class TableRow:
    def __init__(self, data_waluty, kwota, opis_operacji):
        self.data_waluty = data_waluty
        self.kwota = kwota
        self.opis_operacji = opis_operacji


def print_csv():
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('Data', 'Kwota', 'Tag', 'Opis'))

    with open(input, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = True  # zmienna pomocnicza do pominięcia nagłówka
        for row in reader:
            # print(row)
            if header:  # pomijamy nagłówek
                print(row)
                header = False
            else:
                data.append(row)
    data_reversed = list(reversed(data))
    for row in data_reversed:
        text = row[4]
        text_without_word = re.sub(r' PLN', '', text)
        text_without_word = re.sub(r'-', '', text_without_word)
        print(text_without_word)


# cccccbeeggttfitlbelicjubcehktevllrtdvlbhfebl


def extract_table_content(pdf_path, table_name):
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    table_content = ""
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_content = page.extract_text()
        
        if table_name in text_content:
            start_idx = text_content.find(table_name)
            end_idx = start_idx + len(table_name)
            table_content += text_content[end_idx:]
            
    
    pdf_file.close()
    return table_content






#    file_name = "Wyciąg 31.07.2023.pdf"
#    pdfFileObj = open(file_name, 'rb')
#    fd = open(file_name, "rb")
#    viewer = SimplePDFViewer(fd)
#    data_list = []
#    for canvas in viewer:
#        page_text = canvas.text_content
#
#    print(page_text)

if __name__ == '__main__':
#    print('PyCharm')
#    print_csv()
    # print_pdf()
    pdf_path = "Wyciąg 31.07.2023.pdf"
    table_name = "Wyszczególnienie transakcji"
    # table_content = extract_table_content(pdf_path, table_name)

    # if table_content:
    #     print(table_content)
    # else:
    #     print(f"Table '{table_name}' not found in the PDF.")

    table_data = extract_table_content(pdf_path, table_name)

    # for row in table_data:
        # print(f"Data waluty: {row.data_waluty}, Kwota: {row.kwota}, Opis operacji: {row.opis_operacji}")
