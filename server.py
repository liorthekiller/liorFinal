import socket
import threading
HEADER=64
PORT=5050
# SERVER =socket.gethostname(socket.gethostname())
ADDR=("127.0.0.1",PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

players_sockets = []

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} Connceted.")
    connected=True
    s = "you are player :" + str(len(players_sockets))
    conn.send((s.encode()))
    while connected:
        msg = conn.recv(HEADER).decode()
        # msg_length=int(msg_length)
        # msg=conn.recv(msg_length).decode(FORMAT)
        if msg== DISCONNECT_MESSAGE:
            connected=False
            players_sockets.remove(conn)
            print(conn, " out")
            conn.close()
        else:
            print(f"[{addr}]{msg}")
            conn.send("msg received".encode(FORMAT))
        #
def start():
    server.listen()
    print(f"[listening]sever is listening on {server}")
    while True:
        conn ,addr=server.accept()
        players_sockets.append(conn)
        thread=threading.Thread(target=handle_client,args=(conn ,ADDR))
        thread.start()
        print( f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
print("[starting server...]")
start()