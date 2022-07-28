import zmq

FORMAT = 'utf-8'
PORT = "8080"
HOST = "127.0.0.1"
EXIT = "exit"



context = zmq.Context()
s = context.socket(zmq.SUB)         # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT       # how and where to communicate
s.connect(p)                        # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "OI")   # subscribe to TIME messages





def send(msg):
    #print(f"[SENDING]: {msg}")
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #print(client.recv(2048).decode(FORMAT))


print(s.recv())
run = False
while(run):
    msg = input()
    send (msg)
    print(client.recv(2048).decode(FORMAT))
    if msg == EXIT:
        run = False
