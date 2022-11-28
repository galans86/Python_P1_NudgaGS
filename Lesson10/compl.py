
import math

def calculate_c(n1,n2,op):
    match op:
        case '+': return sum(n1,n2)
        case '-': return sub(n1,n2)
        case '*': return  mult(n1,n2)
        case '/': return div_st(n1,n2)
        case 'pow': return pow(n1,n2)
        case 'sqrt': return sqrt(n1)
        case _: return 'error' 

def sum(n1:complex,n2:complex):
    return n1 + n2

def sub(n1:complex,n2:complex):
    return n1 - n2

def mult(n1:complex,n2:complex):
    return n1 * n2

def div_st(n1:complex,n2:complex): 
    if n2:
        return n1 / n2

def pow(n1:complex,n2:complex):
    p = int(round(n2.real))
    if p >=0:
     return complex( math.pow(n1.real,p) + math.pow(n1.imag,p) * 1j )

def sqrt(n1:complex):
    return complex( math.sqrt(n1.real) + math.sqrt(n1.imag) * 1j )



def complex_view_result(n1:complex,n2:complex, op, result):
    if op == 'sqrt':
        line =  str(f'{op} {n1} = {result}')
    else:
        line = str(f'{n1} {op} {n2} = {result}')
    return line



