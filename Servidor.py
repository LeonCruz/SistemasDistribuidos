"""Implementação do servidor usando sockets."""

import socket

ip = 'localhost'  # Definição do endereço IP
porta = 5000  # Definição da porta de conexão

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Definição do tipo de conexão (TCP ou UDP)
tcp.bind((ip, porta))  # Solicita uma conexão
tcp.listen(1)
print('Servidor: Escutando na porta: {}'.format(porta))

conexao, cliente = tcp.accept()
print('Servidor: Conexão feita com o cliente: {}'.format(cliente))

vetor = conexao.recv(1024)
print(vetor)

conexao.send(vetor)


conexao.close()
