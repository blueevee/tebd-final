import csv
from RO_SUS.model.model import Hospitalizations

with open('D:\BLUEEVEE\TEBD\clean_data\INTERNAMENTOS.csv', 'r', encoding="utf8") as csv_file:
    file = csv.DictReader(csv_file)

    for line in file:
        Hospitalizations.create(
            aih_year=line['ANO_CMPT'],
            aih_month=line['MES_CMPT'],
            specialty=line['ESPEC'],
            aih_number=line['N_AIH'],
            aih_type=line['IDENT'],
            patient_cep=line['CEP'],
            birth_date=line['NASC'],
            patient_sex=line['SEXO'],
            uti_days=int(line['UTI_MES_TO']),
            uti_brand=line['MARCA_UTI'],
            daily_uti=int(line['UTI_INT_TO']),
            daily_hospitalization=int(line['QT_DIARIAS']),
            requested_procedure=line['PROC_SOLIC'],
            procedure_performed=line['PROC_REA'],
            services_cost=float(line['VAL_SH']),
            professionals_cost=float(line['VAL_SP']),
            total_cost=float(line['VAL_TOT']),
            uti_cost=float(line['VAL_UTI']),
            main_diagnosis=line['DIAG_PRINC'],
            city_code=line['MUNIC_MOV'],
            stay_days=int(line['DIAS_PERM']),
            death=line['MORTE'],
            nationality=line['NACIONAL'],
            childrem=int(line['NUM_FILHOS']),
            education_level=line['INSTRU'],
            birth_controll=line['CONTRACEP1'],
            risk_pregnancy=line['GESTRISCO'],
            cnes_code=line['CNES']
        )

csv_file.close()
