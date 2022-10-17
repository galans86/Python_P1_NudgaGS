from os import path
import csv


def export_cont(file: str, contacts: list):
    csv_line = ''
    with open(file, 'w') as m_file:
        for rec in contacts:
            line = ''.join([k+':'+v+' ' for k, v in rec.items()])
            m_file.write(f'{line};\n')
            csv_line += line
    return csv_line


def import_cont(file: str):
    if path.exists(file):
        contacts = []
        n_dict = {}
        with open(file) as m_file:
            csv_line = m_file.read().strip()[:-1]
            n_list = [rec for rec in csv_line.split(sep=';')]
            for i in n_list:
               m_l = i.split( )
               for x in m_l:
                n_dict.setdefault(x.split(':')[0], x.split(sep=':')[1])
            if n_dict:
                contacts.append(n_dict)
    return contacts
