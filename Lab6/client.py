import sys

from gui import ClientAppGUI
from network import ClientAppNetwork


class ClientApp:

    def __init__(self, port, server_ip):
        print("Инициализация клиента, порт: {} , IP: {}".format(port, server_ip))
        self.network = ClientAppNetwork(port, server_ip)
        self.GUI = ClientAppGUI(self.network)

    def run(self):
        if self.network.install():
            self.GUI.install()

    def __del__(self):
        del self.network
        del self.GUI

if __name__ == '__main__':
    run_args = sys.argv[1:]

    port = 8000
    server_ip = 'localhost:8001'

    c = ClientApp(port, server_ip)
    c.run()
