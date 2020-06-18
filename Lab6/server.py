import sys
import socketserver
from server_logic import Parser


class TextCalculatorServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        p = Parser()

        close = False
        while not close:
            data = self.request.recv(1024).decode()
            print("Получено", data)
            # прислали finish - заканчиваем цикл обработки соединения
            if "finish" in data:
                close = True
                print("Подключение завершено")
                continue
            resp = p.process(data)
            print(resp)
            try:
                self.request.sendall(resp.encode())
            except BrokenPipeError:
                continue
            except ConnectionResetError:
                continue


if __name__ == '__main__':

    args = sys.argv[1:]
    port = 8001


    addr = ("localhost", port)

    # создаем TCP сервер для получения

    with socketserver.TCPServer(addr, TextCalculatorServerHandler) as server:
        print("Сервер начал работу на {x[0]}:{x[1]}".format(x=server.server_address))
        try:
            server.serve_forever()
        except:
            print("\nСервен остановлен")
            server.shutdown()
            server.server_close()
