import csv
from RO_SUS.model.model import Cities

with open('D:\BLUEEVEE\TEBD\clean_data\MUNICIPIOS.csv', 'r', encoding="utf8") as csv_file:
    file = csv.DictReader(csv_file)

    for line in file:
        Cities.create(
            city_id = line['COD'],
            city_name=line['NOME']
        )

csv_file.close()
