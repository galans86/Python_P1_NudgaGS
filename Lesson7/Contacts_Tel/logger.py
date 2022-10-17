from datetime import datetime

def write_logs(line):
    time = datetime.now().strftime('%H:%M')
    with open('cont_logs.txt', 'a') as l_file:
        l_file.write('{} {};\n'.format(time,line))
    return line
