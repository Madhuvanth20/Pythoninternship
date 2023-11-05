# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:57:23 2023

@author: madhu
"""

import socket
import threading

# Client configuration
HOST = '127.0.0.1' 
PORT = 65432       

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

threading.Thread(target=receive_messages, args=(client_socket,)).start()

# Send messages
while True:
    message = input()
    client_socket.sendall(message.encode('utf-8'))
    if message == 'exit':
        break

client_socket.close()
