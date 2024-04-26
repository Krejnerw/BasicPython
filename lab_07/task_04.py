import csv
import datetime
def format_data(data):
    data[-1] = data[-1].replace(" z", "").replace(",", ".").replace(" ", "")
    data[2] = str(datetime.datetime.strptime(data[2], '%d.%m.%Y').date())
    return data

with open('zamowienia.csv', errors='ignore', newline='', encoding='utf-8') as f:
    de_file = open('zamowienia_niemcy.csv', 'a', errors='ignore', newline='', encoding='utf-8')
    pl_file = open('zamowienia_polska.csv', 'a', errors='ignore', newline='', encoding='utf-8')
    reader = list(csv.reader(f, delimiter=";"))

    reader = list(map(format_data, reader[1:]))

    header = ";".join(map(str, reader[:1][0])) + "\n"
    pl_file.write(header)
    de_file.write(header)

    for ind, row in enumerate(reader):
        result = ";".join(row) + "\n"
        if row[0] == "Niemcy":
            de_file.write(result)
        elif row[0] == "Polska":
            pl_file.write(result)

    pl_file.close()
    de_file.close()