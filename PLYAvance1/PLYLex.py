#Definicion de tokens
import ply.lex as lex

#Se especifica la lista de tokens disponibles
tokens=[
    # Palabras reservadas
    "DEF","RETURN","TRUE","FALSE","AND","OR",
    # Nombre
    "NOMBRE",
    # Delimitadores
    "LPAREN","RPAREN","LBRACKET","RBRACKET","LBRACE","RBRACE","COLON","COMMA",
    # Operadores
    "EQUALS","MAS","MEN","POR","EXP","DIV","DIVENT",
    # Caracteres especiales
    "SPACE"

]
#[]\
# Ignorar
t_ignore='\t'

# Space
t_SPACE='\s'

# Palabras Reservadas
t_DEF='def'
t_RETURN='return'
t_TRUE='True'
t_FALSE='False'
t_AND='and'
t_OR='or'

# Nombre
t_NOMBRE=r'[a-zA-Z_][a-zA-Z0-9]*'

# Delimitadores
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COLON            = r':'
t_COMMA=r','

# Operadores
t_EQUALS           = r'='
t_MAS=r'\+'
t_MEN=r'-'
t_POR=r'\*'
t_EXP=r'\*\*'
t_DIV=r'/'
t_DIVENT=r'//'

# Define a rule so we can track line numbers
def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

# Error handling rule
#En general, t.lexer.skip(n) omite n caracteres en la cadena de entrada.
def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

"""
Esta parte se encarga de mostrar la informacion del caracter que fue tokenizado
"""
# Give the lexer some input
lex.lex()
data="def sumarDosNUmeros(num1,num2):" \
     "  return num1+num2"
lex.input(data)
# Tokenize
while True:
    tok = lex.token()
    if not tok:
        break      # No more input
    print(tok)