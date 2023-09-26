import csv
from RO_SUS.model.model import Cid

with open('D:\BLUEEVEE\TEBD\clean_data\CID.csv', 'r', encoding="utf8") as csv_file:
    file = csv.DictReader(csv_file)

    for line in file:
        Cid.create(
            cid_id = line['codigo'],
            cid_description=line['descricao']
        )

csv_file.close()
