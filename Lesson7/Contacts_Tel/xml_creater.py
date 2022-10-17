
from os import path
# import xml
# from xml.etree import ElementTree


def export_cont(file: str, contacts: list):
    xml_line = '<xml>\n'
    for rec in contacts:
        xml_line += '  <contact>\n'
        xml_line += '\n'.join(['    <'+k+'>\n      '+v+'\n   </'+k +
                         '>' for k, v in rec.items()])
        xml_line += '\n  </contact>\n'
    xml_line += '</xml>\n'

    with open(file, 'w') as m_file:
        m_file.write(xml_line)
    return xml_line


def import_cont(file: str):
    if path.exists(file):
         contacts = [{}]
                        # в доработке
    return contacts
