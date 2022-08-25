import socket
import threading

HOST_NAME = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST_NAME)
PORT = 5050
DISCONNECT = 'disconnect'
all_clients = []

def remove(client):
   if client in all_clients:
      all_clients.remove(client)
      client.close()

def broadcast_message(message_to_all, sender):
   for client in all_clients:
      if (client != sender):
         try:
            client.send(bytes(message_to_all, 'utf-8'))
         except:
            remove(client)

def handle_client(conn):
   conn.send(bytes('Successfully connected to chat server! \nYour Name ? ', 'utf-8'))
   client_name = conn.recv(1024).decode()
   print(f'{client_name} has entered the chat')

   while True:
      message_from_client = conn.recv(1024).decode()
      try:
         if message_from_client != DISCONNECT:
            message_to_all = '< ' + client_name + ' > ' + message_from_client
            broadcast_message(message_to_all, conn)
         else:
            remove(conn)
      except Exception as e:
         print(f'Error Occurred ! {e}')
         remove(conn)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server)
server.bind((HOST_IP, PORT))
server.listen(10)
print(f'SERVER LISTENING... ON PORT {PORT}')      

while True:
   conn, addr = server.accept()
   print(conn)
   all_clients.append(conn)
   thread_handling_client = threading.Thread(target = handle_client, args = (conn,))
   thread_handling_client.start()   