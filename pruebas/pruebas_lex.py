
##### ALGORITMOS DE PRUEBA LEXICO #####

## Johnny Santiago Rodriguez Salinas

def test_vars_declaration():
    return '''
            var cadena string      
            var numero int
            var numero1 float32
            var numero2 float64
            var bool1 bool
            '''

def test_for_body():
    return '''
           for i := 0; i < 5; i++ {
           
           }
           '''

def test_if_sin_else():
    return '''
           if (-8 == .9){
        
           }
           '''

def test_if_con_else():
    return '''
           if(-.7>.23){
                return true
           }else{
                return false
           }
           '''

def test_func_declaration():
    return '''
           func main(a int,b int){
                return a + b 
           }
           '''

def test_switch_declaration():
    return '''
           switch valor {
                case 1:
                    // codigo
                case 2:
                    // codigo
                case 3:
                    // codigo
                default:
                    // codigo
            }
           '''

##  Jeremy Martinez
def test_suma_expression():
    return '''
        resultado = x + y
        a = b + c
        '''

def test_resta_expression():
    return '''
        resultado = x - y
        a = b - c
        '''

def test_multiplicacion_expression():
    return '''
        resultado = x * y
        a = b * c
        '''

def test_division_expression():
    return '''
        resultado = x / y
        a = b / c
        '''

def test_incremento_expression():
    return '''
        b = c++
        x++
        '''

def test_decremento_expression():
    return '''
        b = c--
        x--
        '''

#### Nicolas Coronel ####

def test_mayorQue():
    return '''
        z > 10
        a > b
        c>10
        '''
def test_menorQue():
    return '''
        1 < 10
        a < b
        '''
def test_menorIgualQue():
    return '''
        10 <= 10
        a<=b
        '''
def test_mayorIgualQue():
    return '''
        10 >= 10
        a>=b
        '''
def test_diferenteQue():
    return '''
        z != 10
        a != b
        '''
def test_igualQue():
    return '''
        z == 10
        a == b
        '''
def test_modulo():
    return '''
        z % 10
        3 % w
        a % y
        25 % 5
        '''