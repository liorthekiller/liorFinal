import socket

HEADER=64
PORT=5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
server="192.168.1.26"
addr=(server,PORT)
# my_socket = None
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def start():
    my_socket.connect(("127.0.0.1",5050))
    print(my_socket.recv(1024).decode())
    play()
    # p = player_first_screen.main()

def play():
    while True:
        msg = input("Enter a message: ")
        message=msg.encode(FORMAT)
        my_socket.send(message)
        if msg == DISCONNECT_MESSAGE:
            print ("you are out ")
            my_socket.close()
            break

start()