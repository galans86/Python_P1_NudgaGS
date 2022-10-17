contacts = []

def add_contacts():
    global contacts   
    
    n_c = { 'name1': input('Фамилия: '), 
            'name2': input('Имя: '), 
            'tel':   input('Телефон: '),
            'desc':  input('Описание: ') }
    contacts.append(n_c)

def get_contacts():
    return contacts

def set_contacts(new_contacts):
    global contacts  
    # contacts.append(new_contacts)
    contacts = new_contacts
