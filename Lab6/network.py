import socket


class ClientAppNetwork:

    def __init__(self, port, server_ip):
        addr = server_ip.split(":")
        self.server_addr = addr[0], int(addr[1])
        self.host = "localhost"
        self.port = port
        self.socket = None
        self.conn = None

    def install(self):

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(2)
        except socket.error:
            print("Ошибка создания сокета")
            return False

        try:
            self.conn = self.socket.connect(self.server_addr)
        except socket.error:
            print("Ошибка подключения к серверу")
            self.socket.close()
            self.socket = None
            return False
        print("Подключен")
        return True

    def send_to_server(self, data: str) -> str or None:

        if self.socket:
            try:
                self.socket.send(data.encode())
                print("Отправлено", data)
            except socket.timeout:
                return "Ошибка отправки"
            try:
                response = self.socket.recv(1024)
                print("Получено", response.decode())
                return response.decode()
            except socket.timeout:
                print("Большое время отклика")

        else:
            return None

    def __del__(self):
        self.send_to_server('finish')
        if self.conn is not None:
            self.conn.close()
        if self.socket is not None:
            self.socket.close()
            print("CLOSED")