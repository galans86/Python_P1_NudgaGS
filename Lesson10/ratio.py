
import math

def calculate_r(n1,n2,op):
    match op:
        case '+': return sum(n1,n2)
        case '-': return sub(n1,n2)
        case '*': return  mult(n1,n2)
        case '/': return div_st(n1,n2)
        case 'pow': return pow(n1,n2)
        case 'sqrt': return sqrt(n1)
        case '//': return div(n1,n2)
        case '%': return mod(n1,n2)
        case _: return 'error' 

def sum(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div_st(n1,n2):  # обычное деление
    if n2:
        return n1 / n2

def div(n1,n2):  # целое
    return n1 // n2

def mod(n1,n2):  # остаток
    return n1 % n2

def pow(n1,n2):
    if n2 >= 0:
       p = int(round(n2))
    return math.pow(n1,p)
    
def sqrt(n1):
    return math.sqrt(n1)  


def ratio_view_result(n1,n2, op, result):
    if op == 'sqrt':
        line =  str(f'{op} {n1} = {result}')
    else:
        line = str(f'{n1} {op} {n2} = {result}')
    return line

