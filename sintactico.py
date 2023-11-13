# Yacc import
import ply.yacc as yacc
# Token map from the lexer
from lexico import tokens

def p_sentencia(p):
    '''sentencia : impresion
                | asignacion
                | declaracionVariable
                | estructura
                '''


def p_estructura(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY asignacion RKEY'

def p_estructura_vacia(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY RKEY'

def p_declaracionVariable(p):
    '''variable : VAR IDENTIFICADOR STRING ASSIGN valor
                | VAR IDENTIFICADOR INT ASSIGN valor
                | VAR IDENTIFICADOR FLOAT32 ASSIGN valor
                | VAR IDENTIFICADOR FLOAT64 ASSIGN valor
                | VAR IDENTIFICADOR BOOL ASSIGN valor
                '''

def p_declaracionVariable_vacia(p):
    '''variable : VAR IDENTIFICADOR INT
                | VAR IDENTIFICADOR STRING
                | VAR IDENTIFICADOR FLOAT32
                | VAR IDENTIFICADOR FLOAT64
                | VAR IDENTIFICADOR BOOL
                '''
def p_declaracionVariable_simple(p):
    '''variable : IDENTIFICADOR COLLON ASSIGN ENTERO
                | IDENTIFICADOR COLLON ASSIGN IDENTIFICADOR
                | IDENTIFICADOR COLLON ASSIGN BOOL
                | IDENTIFICADOR COLLON ASSIGN FLOTANTE
                '''
def p_declaracionVariable_estructura(p):
    '''variable : IDENTIFICADOR INT
                | IDENTIFICADOR STING
                | IDENTIFICADOR FLOAT32
                | IDENTIFICADOR FLOAT64
                | IDENTIFICADOR BOOL
                '''

def p_asignacion(p):
    '''asignacion : IDENTIFICADOR ASSIGN valores
                    '''

def p_impresion(p):
    "impresion : IMPRIMIR LPAREN valores RPAREN "

def p_impresion_sin_valor(p):
    'impresion : IMPRIMIR LPAREN RPAREN'

def p_valores(p):
    '''valores : valor
                | valor COMA valores
                '''
def p_valor(p):
    '''valor : ENTERO
            | FLOTANTE
            | STRING
            | BOOL
            | IDENTIFICADOR
            '''
    
def p_error(p):
    print("Error de sintaxis")

'''
# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('>>> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result != None:
       print(result)
       '''