
from importlib.resources import path
from os import path
import json


def export_cont(file: str, contacts: list):
    json_line = json.dumps(*contacts)
    # if path.exists(file):
    with open(file, 'w') as m_file:
        m_file.write(json_line)
    return json_line


def import_cont(file: str):
    if path.exists(file):
        with open(file) as m_file:
            json_line = m_file.read().strip()
            if json_line:
                contacts = json.loads(json_line)
    return contacts
