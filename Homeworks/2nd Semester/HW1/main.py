class Server:
    def __init__(self, buffer, ip):
        buffer = buffer
        ip = ip

    def send_data(self):
        pass

    def get_data(self):
        pass

    def get_ip(self):
        pass

class Router:
    def link(self, server):
        pass

    def unlinck(self, server):
        pass





class Data:
    def __init__(self, data: str, ip_addrs: str):
        self.data = data
        self.ip_addrs = ip_addrs

if __name__ == "__main__":
    server = Server()
    router = Router()
    data = Data("Данные", '192.168.0.1')
