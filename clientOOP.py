import socket

HEADER=64
PORT=5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
server="192.168.1.26"
addr=(server,PORT)
# my_socket = None

class clientOOP:
    def __init__(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect(("127.0.0.1", 5050))
        print("Client Created")
        print(self.my_socket.recv(1024).decode())
        self.__handle_connection__()

    def __handle_connection__(self):
        while True:
            msg = self.my_socket.recv(1024).decode()
            print("received message", msg)
#
# def start():
#
#     play()
#     # p = player_first_screen.main()

    def send_message(self, msg):
        while True:
            msg = input("Enter a message: ")
            msg=msg.encode(FORMAT)
            self.my_socket.send(msg)
            if msg == DISCONNECT_MESSAGE:
                print ("you are out ")
                self.my_socket.close()
                # break

