from ply import yacc
from lexer import tokens, MyLexer  # Import tokens and lexer from your lexer file

# Instantiate the lexer
lexer = MyLexer()

# Define the parser
def p_sql_injection(p):
    '''sql_injection : username condition
                     | username comment'''
    p[0] = (p[1], p[2])

def p_username(p):
    'username : USERNAME'
    p[0] = p[1]

def p_condition(p):
    'condition : QUOTE OR QUOTE STATEMENT'
    print("Parsing condition rule")
    print(f"p[7].type: {p[7].type}")
    print(f"p[7].value: {p[7].value}")
    p[0] = ('condition', p[4], p[7])

def p_column(p):
    'column : QUOTE column_value QUOTE'
    p[0] = p[2]

def p_column_value(p):
    'column_value : VALUE'
    print("Parsing column_value rule")
    print(f"p[1].type: {p[1].type}")
    print(f"p[1].value: {p[1].value}")
    p[0] = p[1]

def p_comment(p):
    'comment : COMMENT'
    print("Parsing comment rule")
    print(f"p[1].type: {p[1].type}")
    print(f"p[1].value: {p[1].value}")
    p[0] = ('comment', p[1].value)

# Add a p_error function
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {find_column(p)}: Unexpected token {p.type}, value {p.value}")

def find_column(token):
    last_cr = lexer.lexdata.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column


# Build the parser
parser = yacc.yacc()

# Test the lexer with an example input
data = "admin' or '1'='1"
lexer.input(data)

# Print the tokens produced by the lexer
for token in lexer:
    print(token)

# Test the parser with the example input
parsed_result = parser.parse(data, lexer=lexer)
print(parsed_result)