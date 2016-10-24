import socket

def echo_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 8000)
    s.connect(server_address)

    try:
        message = 'hello from client'
        amount_received = 0
        amount_expected = len(message)
        s.sendall(message)
        while amount_received < amount_expected:
            data = s.recv(10)
            amount_received += len(data)
            print 'received {0}'.format(data)
    except socket.error as e:
        print e
    except Exception as e:
        pass
    finally:
        s.close()

if __name__ == '__main__':
    echo_client()
