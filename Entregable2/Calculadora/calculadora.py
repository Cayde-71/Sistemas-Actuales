from datetime import datetime

#Semantica:

# R = resultado anterior

#sumar: + a b
#restar: - a b
#multiplicar: * a b
#dividir: / a b
#Potencia: ^ a b
#Media: m a b

class calculadora():

    def __init__(self):
        self.resultado = 0
        print(datetime.now(), "[Info] Nueva conexion creada: ", self)

    def operar(self,mensaje:str):
        if not mensaje:
            return
        solicitude = self.parser(mensaje)
        if len(solicitude) != 3:
            print(datetime.now(), "[Error] Numero incorrecto de argumentos: ", mensaje)
            return "Error: Numero incorrecto de argumentos"

        response = self.calcular(solicitude)
        self.resultado = response
        print(datetime.now(), '[Info] Operacion Completada.', mensaje, '-->', response)
        return str(response)

    def reset(self):
        self.resultado = 0
        print(datetime.now(), "[Info] Resultado reiniciado para la conexion: ", self)
        return "Resultado reiniciado"

    def get_result(self):
        return self.resultado

    def parser(self, mensaje:str):
        return mensaje.split()

    def calcular(self, op):
        match op[0]:
            case '+':
                if op[1] == 'R':
                    return self.sumar(self.resultado,int(op[2]))
                else:
                    return self.sumar(int(op[1]),int(op[2]))
            case '-':
                if op[1] == 'R':
                    return self.restar(self.resultado,int(op[2]))
                else:
                    return self.restar(int(op[1]),int(op[2]))
            case '*':
                if op[1] == 'R':
                    return self.multiplicar(self.resultado,int(op[2]))
                else:
                    return self.multiplicar(int(op[1]),int(op[2]))
            case '/':
                if op[1] == 'R':
                    return self.dividir(self.resultado,int(op[2]))
                else:
                    return self.dividir(int(op[1]),int(op[2]))
            case '^':
                if op[1] == 'R':
                    return self.potencia(self.resultado,int(op[2]))
                else:
                    return self.potencia(int(op[1]),int(op[2]))
            case 'm':
                if op[1] == 'R':
                    return self.media(self.resultado,int(op[2]))
                else:
                    return self.media(int(op[1]),int(op[2]))
            case _:
                return "Error: Operacion no soportada"

    def sumar(self, a:int,b:int):
        return a+b

    def restar(self, a:int,b:int ):
        return a-b

    def multiplicar(self, a:int,b:int):
        return a*b

    def dividir(self, a:int,b:int):
        if b == 0:
            return "Error: Division por cero"
        return a/b

    def potencia(self, a:int,b:int):
        return a**b

    def media(self, a:int,b:int):
        return (a+b)/2