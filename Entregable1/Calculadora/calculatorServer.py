import socketserver
import threading
from datetime import datetime

import calculadora


class MiServidor(socketserver.TCPServer):
    active_connections = 0
    lock = threading.Lock()

    def add_connection(self):
        with self.lock:
            self.__class__.active_connections += 1
            print(datetime.now(), f"[Info] Conexiones activas: {self.__class__.active_connections}")

    def remove_connection(self):
        with self.lock:
            self.__class__.active_connections -= 1
            print(datetime.now(), f"[Info] Conexiones activas: {self.__class__.active_connections}")

# using netcat or nc commands:
# nc localhost 5088
# nc -v localhost 5088

# is the port used?
# lsof -i -P -n | grep 5088