import socket
import threading

SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
PORT = 5050

def handle_sending_msgs():
   while True:
      message = input()
      client.send(bytes(message, 'utf-8'))

def handle_receiving_msgs():
   while True:
      print(client.recv(1024).decode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
client.connect((SERVER_IP, PORT))
server_initial_response = client.recv(1024).decode()
client_name = input(server_initial_response)
client.send(bytes(client_name, 'utf-8'))

thread_handling_sending = threading.Thread(target = handle_sending_msgs)
thread_handling_sending.start()

thread_handling_receiving = threading.Thread(target = handle_receiving_msgs)
thread_handling_receiving.start()