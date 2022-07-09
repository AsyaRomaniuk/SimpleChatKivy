import socket


# 192.168.1.14 DESKTOP-OADG3PC

def receive():
    while True:
        client, address = server.accept()
        print("Приєднався клієнт: {}".format(str(address)))
        command = client.recv(1024).decode('utf-8')
        print(f"Прийшла команда: {command!r} !")


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 50284))
    server.listen()
    print("Слухаю...")
    receive()
