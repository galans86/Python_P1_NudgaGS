# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def get_dict(names:str):
    l_d = [ n[:1] for n in names ]
    l_d.sort()
    m_dict = {}.fromkeys(l_d,[])
    for k,v in m_dict.items():
        v = [n for n in names if n[:1] == k]
        m_dict.update({k:v})
    return m_dict

names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка", "Галочка"]
print(get_dict(names))