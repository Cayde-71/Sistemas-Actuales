import socketserver
from datetime import datetime

#Semantica:

#sumar: + a b
#restar: - a b
#multiplicar: * a b
#dividir: / a b
#Potencia: ^ a b
#Media: m a b

conexiones = 0 #Contador de conexiones activas

class calculadora(socketserver.StreamRequestHandler):

    def handle(self):
        self.server.add_connection()  # Incrementar el contador de conexiones activas
        try:
            mensaje = self.rfile.readline().decode("utf-8").strip()
            if not mensaje:
                return

            solicitude = self.parser(mensaje)
            if len(solicitude) != 3:
                print(datetime.now(), "[Error] Numero incorrecto de argumentos: ", mensaje)
                self.wfile.write(b"Error: Numero incorrecto de argumentos")
                return

            response = str(self.calcular(solicitude))
            print(datetime.now(), '[Info] Operacion Completada.', mensaje, '-->', response)
            self.wfile.write(response.encode("utf-8"))
        except ConnectionResetError:
            print(datetime.now(), "[Error] Conexion cerrada por el cliente.")
        finally:
            self.server.remove_connection() 

    def parser(self, mensaje:str):
        return mensaje.split()

    def calcular(self, op):
        match op[0]:
            case '+':
                return self.sumar(int(op[1]),int(op[2]))
            case '-':
                return self.restar(int(op[1]),int(op[2]))
            case '*':
                return self.multiplicar(int(op[1]),int(op[2]))
            case '/':
                return self.dividir(int(op[1]),int(op[2]))
            case '^':
                return self.potencia(int(op[1]),int(op[2]))
            case 'm':
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