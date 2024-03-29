#### ALGORITMOS DE PRUEBA SINTACTICO ####
import random

def test_impresion():
    return 'fmt.Println(carro)'

def test_impresion_vacia():
    return 'fmt.Println()'

def test_ingreso():
    return 'fmt.Scanln(nombre)'

def test_ingreso_vacio():
    return 'fmt.Scanln()'

def test_declaracion_variable():
    return 'var nombre string = henry'

def test_declaracion_variable_vacia():
    return 'var edad int'

def test_declaracion_variable_simple():
    return 'nombre := enrique'

def test_funcion_parametros_return():
    return 'func suma (carro string) string{ fmt.Println(carro) return carro}'

def test_funcion_parametros():
    return 'func suma (carro string){ fmt.Println(carro)}'

def test_funcion_return():
    return 'func suma ()int{ fmt.Println(carro) return numero}'

def test_funcion():
    return ' func suma (){ fmt.Println(carro)}'

def test_estructura():
    return 'type persona struct { edad int}'

def test_estructura_vacia():
    return 'type coche struct { } '

def test_if():
    return 'if variable>9.2 || go>=8 { fmt.Println(variable) ; var nombre string = henry }'

def test_if_condicion_unica():
    return 'if go>=8 { fmt.Println(variable) }'

def test_suma():
    opciones = ['aha + ehe', '4526 + 8940', 'hej + 89']
    resultado = random.choice(opciones)
    return resultado
def test_resta():
    opciones = ['alw - gg', '46 - 2', 'je - 89']
    resultado = random.choice(opciones)
    return resultado    
def test_multiplicacion():
    opciones = ['wjrh * vcn', '20 * 11', 'pas * 89']
    resultado = random.choice(opciones)
    return resultado
def test_division():
    opciones = ['apaq / jehr','987 / 55' ,'pqie / 89']
    resultado = random.choice(opciones)
    return resultado
def test_incremento():
    return 'hegrg ++'
def test_decrementi():
    return 'qoeu --'