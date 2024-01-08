from lexer import tokens
from ply import yacc
import tracemalloc

tracemalloc.start()

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
  if p:
      print(f"Syntax error at token {p.type}")
  else:
      print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()
print('---SQL INJECTION---')
with open('parserinjection.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    result = parser.parse(line)
    if result:
      print(f" SQL Injection: {line}")
    else:
      print(f"Not SQL Injection: {line}")
      
print('---NOT SQL INJECTION---')
with open('parsersafe.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    result = parser.parse(line)
    if result:
      print(f" SQL Injection: {line}")
    else:
      print(f"Not SQL Injection: {line}")


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

