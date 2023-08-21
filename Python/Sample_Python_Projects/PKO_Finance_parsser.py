import csv
import re

data = []
input_csv = 'lista_operacji_230401_230419_202304191524525552.csv'


def print_csv():
    print("{:<10} {:<10} {:<10} {:<10}".format('Data', 'Kwota', 'Tytuł', 'Konto'))

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


if __name__ == '__main__':
    print('PyCharm')
    print_csv()