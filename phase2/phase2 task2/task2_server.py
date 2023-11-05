# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:57:09 2023

@author: madhu
"""

import socket
import threading

# Server configuration
HOST = '127.0.0.1'  
PORT = 65432        


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []


def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message == "exit":
            clients.remove(client_socket)
            client_socket.sendall("You have left the chat.".encode('utf-8'))
            break
        print(f"Received message from {address}: {message}")
        for client in clients:
            if client != client_socket:
                client.sendall(f"{address}: {message}".encode('utf-8'))

    client_socket.close()


def accept_incoming_connections():
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")
        client_socket.sendall("Welcome to the chat! Type 'exit' to leave.".encode('utf-8'))
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, address)).start()


print("Server is listening for incoming connections...")
accept_incoming_connections()
