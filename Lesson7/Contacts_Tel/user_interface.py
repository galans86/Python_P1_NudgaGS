import imp

import data_provider as dt
import csv_creater as cc
import json_creater as jc
import xml_creater as xc
import logger

mode = 0

def contacts_run():
    print('\n--Contacts--\n')
    while menu():
        match get_mode():
            case 1:
                dt.add_contacts()
            case 2:
                cc.export_cont('cont_csv.csv',dt.get_contacts())
                logger.write_logs('CSV export')
            case 3:
                dt.set_contacts(cc.import_cont('cont_csv.csv'))
                logger.write_logs('CSV import')
            case 4:
                jc.export_cont('cont_json.json',dt.get_contacts())
                logger.write_logs('JSON export')
            case 5:
                dt.set_contacts(jc.import_cont('cont_json.json'))
                logger.write_logs('JSON import')
            case 6:
                xc.export_cont('cont_xml.xml',dt.get_contacts())
                logger.write_logs('XML export')
            case 7:
                dt.set_contacts(xc.export_cont('cont_xml.xml'))
                logger.write_logs('XML import')
            case 8:
                contacts_view()
            case _:
                print('end')
                break
        

def menu():
    global mode
    mode = int(input('Working with:\n'
                     '1 - Add Contacts\n'
                     '2 - CSV  export\n'
                     '3 - CSV  import\n'
                     '4 - JSON export\n'
                     '5 - JSON import\n'
                     '6 - XML  export\n' 
                     '7 - XML  import\n' 
                     '8 - View Contacts\n'
                     '0 - exit\n'))
    if mode not in [0,1,2,3,4,5,6,7,8]:
        mode = 0
        print('Input incorrect\n')
    return mode

def get_mode():
    return mode


def contacts_view():
    for i in dt.get_contacts():
        line = ' '.join(i.values())
        print(f'{line};\n')