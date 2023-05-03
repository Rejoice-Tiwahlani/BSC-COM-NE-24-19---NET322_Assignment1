import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server():
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, 9090)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print ("Waiting to receive message from client")
        client, address = sock.accept()
        while True:
            data = client.recv(data_payload)
            if data:
                message = data.decode('utf-8')
                print ("Data: %s" %message)
                if message == 'quit':
                    break
                client.send(data)
                print ("sent %s bytes back to %s" % (data, address))
            else:
                break
        # end connection
        client.close()
        if message == 'quit':
            break

    # close the socket
    sock.close()

if __name__ == '__main__':
    echo_server()
