import xmlrpc.client
import socket

client = xmlrpc.client.ServerProxy('http://localhost:8000')

def request_file(filename, client_ip):
    try:
        content = client.send_file(filename, client_ip)
        with open(filename, 'wb') as file:
            file.write(content.data)
        print("File received and saved as", filename)
    except Exception as e:
        print(str(e))

def send_file(filename, client_ip):
    try:
        with open(filename, 'rb') as file:
            content = xmlrpc.client.Binary(file.read())
            result = client.receive_file(filename, content, client_ip)  
            print(result)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    client_ip = socket.gethostbyname(socket.gethostname())

    while True:
        action = input("What do you want to do? (send/request/quit)")
        if action == "send":
            name = input("What is the name of the file you want to send?")
            send_file(name, client_ip)
        elif action == "request":
            name = input("What is the name of the file you want to request?")
            request_file(name, client_ip)
        elif action == "quit":
            break
        else:
            print("Select the proper action")
    

