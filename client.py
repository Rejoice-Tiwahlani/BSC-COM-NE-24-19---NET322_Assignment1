import socket
import sys

host = 'localhost'


def echo_client():
    """ A simple echo client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, 9090)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # Send and receive data
    try:
        while True:
            # Prompt the user for input
            input1 = input("Enter what you want to send to server (type 'quit' to exit): ")
            if input1 == 'quit':
                break
            message = input1
            print("Sending %s" % message)
            sock.sendall(message.encode('utf-8'))
            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print("Received: %s" % data)
    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    echo_client()
