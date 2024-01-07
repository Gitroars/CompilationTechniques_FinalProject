from ply import lex
import re
tokens = ('USERNAME', 'QUOTE', 'EQUAL', 'VALUE', 'OR', 'COMMENT')


def MyLexer():

 def t_OR(t):
  r'(?i)or'
  return t

 def t_VALUE(t):
  r'\d+'
   # Convert the matched text to an integer
  return t
 
 t_USERNAME = r'[a-zA-Z0-9_][a-zA-Z0-9_.]*'
 t_QUOTE = r"'"
 t_EQUAL = r'='
 t_COMMENT = r'--.*'
 t_ignore = ' \t'

 def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

 def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

 # Build the Lexer
 return lex.lex()


# Test the lexer with an example input
lexer = MyLexer()

data = "admin' or '1'='1"
data6 = "admin' or ''='"
data9 = "'--"
data10 = "'1'='1 or admin'"

lexer.input(data)



testRegex = r'\t'

for token in lexer:
 print(token)

  