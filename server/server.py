from xmlrpc.server import SimpleXMLRPCServer
import os
import datetime

server = SimpleXMLRPCServer(('0.0.0.0', 8000))

def log(action, filename, client_address):
    log_file = "server.log"
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, 'a') as file:
            newLog = f'[{client_address}][{formatted_time}] - {action} - {filename}\n'
            file.write(newLog)
    except Exception as e:
        return str(e)

def send_file(filename, client_ip):
    folder_path = 'request/'
    file_path = os.path.join(folder_path, filename)
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            log('Sent', filename, client_ip)
        return content
    except Exception as e:
        return str(e)

def receive_file(filename, content, client_ip):
    folder_path = "storage/"
    file_path = os.path.join(folder_path, filename)
    try:
        with open(file_path, 'wb') as file:
            file.write(content.data)
            log('Received', filename, client_ip)
        return f"File {filename} received and saved on the server."
    except Exception as e:
        return str(e)

server.register_function(send_file, 'send_file')
server.register_function(receive_file, 'receive_file')

print("Server is ready to accept requests.")
server.serve_forever()

