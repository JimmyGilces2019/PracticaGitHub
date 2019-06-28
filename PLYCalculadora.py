from ply import lex
import ply.yacc as yacc
"""
tokenizar la entrada, lo que significa que buscó los símbolos que constituyen la expresión aritmética
analizar , lo que implica analizar los tokens extraídos y evaluar el resultado.
"""
# List of token names. This is always required, son todos los posibles nombres que nos da el lexer
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Regular expression rules for simple tokens. Siempre tiene el prefijo t_ para hacer coincidir tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

"""
t.type que es el tipo de token (como una cadena) (por ejemplo: 'NUMBER' , 'PLUS' , etc.). 
Por defecto, t.type se establece en el nombre que sigue al prefijo t_ .
t.lexpos que es la posición del token en relación con el comienzo del texto de entrada.
Si no se devuelve nada de una función de regla de expresiones regulares, el token se descarta. 
Si desea descartar un token, alternativamente puede agregar el prefijo t_ignore_ a una variable de regla de expresiones
regulares en lugar de definir una función para la misma regla.   t_ignore_COMMENT = r'\#.*'
"""

# A regular expression rule with some action code
# Acepta un argumento que es una instancia lexToken y devuelve el mismo
def t_NUMBER( t ) :
    r'[0-9]+' #Expresiones regulares para hacer coincidir los tokens
    t.value = int( t.value )#t.value que es el lexema (el texto real t.value )
    return t


"""
t.lineno que es el número de línea actual (esto no se actualiza automáticamente, ya que el lexer no sabe nada de los números de línea).
 Actualiza lineno usando una función llamada t_newline .
"""
# Define a rule so we can track line numbers
def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

# Error handling rule
#En general, t.lexer.skip(n) omite n caracteres en la cadena de entrada.
def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )


# Build the lexer
lexer = lex.lex()
"""
Esta parte se encarga de mostrar la informacion del caracter que fue tokenizado
"""
# Give the lexer some input
data=input("DATOS DE ENTRADA: ")
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

"""
Los literales son tokens que se devuelven como son. Tanto t.type como t.value se establecerán en el propio carácter. 
Defina una lista de literales como tales:
literals = [ '+', '-', '*', '/' ] o literals = "+-*/"
"""
#**********************************************************************************************************************
precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]

def p_mult_div( p ) :
    '''expr : expr TIMES expr
            | expr DIV expr'''

    if p[2] == '*' :
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()
#"-4*-(3-5)"
res = parser.parse(input("Ingrese expresion: ")) # the input
print(res)