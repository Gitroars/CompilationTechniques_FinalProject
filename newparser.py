from lexer import tokens
from ply import yacc


def p_sql_injection(p):
  '''
    sql_injection : username condition
                  | username COMMENT
    '''
  p[0] = p[1] + p[2]


def p_condition(p):
  '''
  condition : simple_condition
            | complex_condition
           
  '''
  p[0] = " ".join(p[1:])


def p_username(p):
  '''
  username : USERNAME
            | empty
  '''
  p[0] = p[1]


def p_empty(p):
  '''
  empty :
  '''
  p[0] = ""


def p_simple_condition(p):
  '''
  simple_condition : QUOTE COMMENT
  '''
  p[0] = " ".join(p[1:])


def p_complex_condition(p):
  '''
  complex_condition :  QUOTE OR QUOTE VALUE QUOTE EQUAL QUOTE VALUE 
                          | QUOTE OR QUOTE QUOTE EQUAL QUOTE  
  '''
  p[0] = " ".join(p[1:])


def p_error(p):
  print(f"Syntax error at token {p.type}")


# Build the parser
parser = yacc.yacc()

# Test the parser with some input
data1 = "'or''='"
data2 = "'or'1'='1"
data3 = "user'or'1'='1"
data4 = "user' or ''='"
data5 = "admin' or '1'='1"
data6 = "admin' or ''='"
data7 = "'--"
data8 = "user'--"
data9 = "admin'--"
data10 = "vsauce34659'or ''='"
data11 = "vsauce34659' or '3'='3"
data12 = "vsauce34659'--"

allData = [
    data1, data2, data3, data4, data5, data6, data7, data8, data9, data10,
    data11, data12
]

for data in allData:
  result = parser.parse(data)
  print(result)
  if result:
    print(f" SQL Injection in {data}")
  else:
    print(f"No SQL Injection in {data}")
