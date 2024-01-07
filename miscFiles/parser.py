import ply.yacc as yacc

from lexer import MyLexer

tokens = ['USERNAME', 'QUOTE', 'EQUAL', 'VALUE', 'OR', 'COMMENT']
# Regular expression rules for tokens
t_USERNAME = r'[a-zA-Z0-9_][a-zA-Z0-9_.]*'
t_QUOTE = r"'"
t_EQUAL = r'='
t_VALUE = r'[0-9]+'
t_OR = r'or'
t_COMMENT = r'--.*'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
# Build the lexer
lexer = MyLexer()

# Define the starting rule
start = 'sql_injection'


# Define the grammar rules
def p_sql_injection(p):
  '''
  sql_injection : USERNAME condition
                | USERNAME COMMENT
  '''
  if (len(p[2]) == 4):
    p[0] = p[2]
  else:
    raise Exception("Unexpected condition in SQL injection")


def p_condition(p):
  '''
  condition : QUOTE OR QUOTE statement' | QUOTE OR QUOTE VALUE QUOTE
  '''
  
  # p[0] = "or" + p[4]
  # if len(p) == 5:
  #   p[0] = f"or {p[4]}"
  # elif len(p) == 7:
  #   p[0] = "or ''" + str(p[3])
  # else:
  #   raise Exception("Unexpected condition in SQL injection")

  if p[4] == 'USERNAME':
    p[0] = f"or {p[4]}"
  else:
    p[0] = f"or {p[4]}"

def p_statement(p):
  'statement : QUOTE VALUE QUOTE EQUAL QUOTE VALUE QUOTE'
  p[0] = f"'{int(p[2])}' = '{int(p[6])}'"


def p_error(p):
  print("Syntax error at '%s'" % p.value)


# Build the parsert
parser = yacc.yacc(lexer)

# Test the parser with an example input
data = "' or ''='"
result = parser.parse(data, lexer=lexer)
print(result)