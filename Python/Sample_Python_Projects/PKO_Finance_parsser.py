import csv
import re
import pdfreader

from pdfreader import PDFDocument, SimplePDFViewer


data = []
input_csv = 'lista_operacji_230401_230419_202304191524525552.csv'



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


def print_pdf():

    file_name = "Wyciąg 31.07.2023.pdf"
    fd = open(file_name, "rb")
    viewer = SimplePDFViewer(fd)
    data_list = []

    for canvas in viewer:
        page_text = canvas.text_content
        data_list.append(page_text)

    for page_num, page_text in enumerate(data_list, start=70):
        print(f"Page {page_num}:\n{page_text}\n")

    fd.close()

print_pdf()
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
    print_pdf()
