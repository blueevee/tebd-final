import csv
from RO_SUS.model.model import Establishments

with open('D:\BLUEEVEE\TEBD\clean_data\ESTABELECIMENTOS.csv', 'r', encoding="utf8") as csv_file:
    file = csv.DictReader(csv_file)

    for line in file:
        Establishments.create(
            cnes_id=line['CNES'],
            cnes_cep=line['COD_CEP'],
            cnes_turn=line['TURNO_AT'],
            cnes_urgency=line['URGEMERG'],
            outpatient_care=line['ATENDAMB'],
            surgery_center=line['CENTRCIR'],
            obstetric_center=line['CENTROBS'],
            neonatal_center=line['CENTRNEO'],
            hopital_care=line['ATENDHOS'],
            own_social_service=line['SERAP02P'],
            third_social_service=line['SERAP02T'],
            own_pharmacy=line['SERAP03P'],
            third_pharmacy=line['SERAP03T'],
            own_sterilization_materials=line['SERAP04P'],
            third_sterilization_materials=line['SERAP04T'],
            own_nutrition=line['SERAP05P'],
            third_nutrition=line['SERAP05T'],
            own_lactarian=line['SERAP06P'],
            third_lactarian=line['SERAP06T'],
            own_milk_bank=line['SERAP07P'],
            third_milk_bank=line['SERAP07T'],
            own_laudry=line['SERAP08P'],
            third_laudry=line['SERAP08T'],
            own_maintence=line['SERAP09P'],
            third_maintence=line['SERAP09T'],
            own_ambulance=line['SERAP10P'],
            third_ambulance=line['SERAP10T'],
            own_morgue=line['SERAP11P'],
            third_morgue=line['SERAP11T'],
            biological_waste_collection=line['RES_BIOL'],
            chemical_waste_collection=line['RES_QUIM'],
            radioactive_waste_collection=line['RES_RADI'],
            medical_ethics=line['COMISS01'],
            nursing_ethics=line['COMISS02'],
            hospital_infection_control=line['COMISS04'],
            death_analysis=line['COMISS09'],
            disease_notification=line['COMISS11'],
            zoonoses_control=line['COMISS12'],
            sus_hospitalization=line['AP01CV01'],
            sus_ambulatory_care=line['AP02CV01'],
            sus_sadt=line['AP03CV01'],
            sus_urgency=line['AP04CV01'],
            sus_others=line['AP05CV01'],
            sus_regulation=line['AP07CV01']
        )

csv_file.close()
