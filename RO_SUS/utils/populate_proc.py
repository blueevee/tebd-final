import csv
from RO_SUS.model.model import Procedure

with open('D:\BLUEEVEE\TEBD\clean_data\PROCEDIMENTOS.csv', 'r', encoding="utf8") as csv_file:
    file = csv.DictReader(csv_file)

    for line in file:
        Procedure.create(
            proc_id=line['codproc'],
            proc_name=line['nome'],
            sex=line['sexo'],
            min_age=int(line['idade_min']),
            max_age=int(line['idade_max']),
            vlr_sp=int(line['vlr_sp']),
            max_quantity=int(line['qtde_maxima']),
            points=int(line['ptos_ato']),
            stay_duration=int(line['dias_permanencia']),
            complexity=line['complexidade'],
            cofunding=line['co_financiamento']
        )

csv_file.close()
