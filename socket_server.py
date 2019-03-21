import socket


def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    valid_id = "abc@gmail.com"
    # valid_id = valid_id.encode().decode()
    valid_pass = "abc123"
    # valid_pass = valid_pass.encode().decode()
    message = " -> Enter the e-mail address:"
    conn.send(message.encode())
    dat = conn.recv(1024).decode()
    # print(dat)
    dat = str(dat)
    # print(dat)
    if not dat:
        conn.close()
    if valid_id == dat:
        message = ' -> Enter the password:'
        conn.send(message.encode())
        dat = conn.recv(1024).decode()
        # print(dat)
        if not dat:
            conn.close()
        if valid_pass != dat:
            message = ' -> Authentication failed. Connection Closed.'
            conn.send(message.encode())
            conn.close()
        else:
            message = 'Credentials Verified. Now you can interact with the server.'
            conn.send(message.encode())
    else:
        message = ' -> Invalid E-mail Id. Connection Closed.'
        conn.send(message.encode())
        conn.close()

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
