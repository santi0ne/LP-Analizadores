# ANALIZADOR LEXICO PARA GO

# Documentación: https://www.dabeaz.com/ply/ply.html

import ply.lex as lex

from pruebas import *

# Palabras Reservadas
reserved = {
   'var':'VAR',  # Johnny Rodriguez

   'int':'INT',          # Johnny Rodriguez 
   'float32':'FLOAT32',  # Johnny Rodriguez  
   'float64':'FLOAT64',  # Johnny Rodriguez   
   'string':'STRING',    # Johnny Rodriguez  
   'bool':'BOOL',        # Johnny Rodriguez
   'for':'FOR',          # Johnny Rodriguez
   'if':'IF',            # Johnny Rodriguez
   'else':'ELSE',        # Johnny Rodriguez
   'func':'FUNC',        # Johnny Rodriguez
   'return':'RETURN',    # Johnny Rodriguez
   'switch':'SWITCH',    # Johnny Rodriguez
   'case':'case'         # Johnny Rodriguez
}

# Secuencia de tokens
tokens = (
    'IDENTIFICADOR',     # Johnny Rodriguez
    'ENTERO',            # Johnny Rodriguez
    'FLOTANTE',          # Johnny Rodriguez
    'ASSIGN',            # Johnny Rodriguez
    'LPAREN',            # Johnny Rodriguez
    'RPAREN',            # Johnny Rodriguez
    'LKEY',              # Johnny Rodriguez
    'RKEY',              # Johnny Rodriguez
    'COLLON',            # Johnny Rodriguez
    'SUMA',              # Jeremy Martinez
    'RESTA',             # Jeremy Martinez
    'MULTIPLICACION',    # Jeremy Martinez
    'DIVISION',          # Jeremy Martinez
    'INCREMENTO',        # Jeremy Martinez
    'DECREMENTO',        # Jeremy Martinez
    'MAYORQUE' ,         # Nicolas Coronel
    'MENORQUE',          # Nicolas Coronel
    'MAYORIGUALQUE',     # Nicolas Coronel
    'MENORIGUALQUE',     # Nicolas Coronel
    'MODULO',            # Nicolas Coronel
    'IGUALQUE',          # Nicolas Coronel
    'DIFERENTEQUE',      # Nicolas Coronel
    'COMA',
    'IMPRIMIR'
)+tuple(reserved.values())

# Expresiones Regulares simples para símbolos
t_IGUALQUE = r'=='
t_ASSIGN = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_COLLON = r':'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MODULO = r'%'
t_DIFERENTEQUE = r'!='
t_COMA = r','

def t_IMPRIMIR(t):
    r'fmt\.Println'
    return t
# Expresiones Regulares para números y variables, incluye cast
def t_IDENTIFICADOR(t):  # Johnny Rodriguez
    r'[a-z_]\w*'
    t.type = reserved.get(t.value,'IDENTIFICADOR')
    return t

def t_FLOTANTE(t):
    r'-?\d*\.\d+'    
    return t

def t_ENTERO(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

# Expresión regular para reconocer saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios, tabulaciones
t_ignore  = ' \t'

# Manejo de errores
def t_error(t):
  print(f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}")
  t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()
'''
# Código para analizar
# code = switch_declaration()
code = test_incremento_expression()
# Enviando el código
lexer.input(code)

# Tokenizar
for token in lexer:
  print(token)

'''