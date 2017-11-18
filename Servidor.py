"""Implementação do servidor usando sockets."""

import socket
from time import sleep


def ordenarVetor(vetorBytes):
    """Função que ordena o vetor."""
    vetor = list(map(int, vetorBytes))

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        m = arr[0]
        return quicksort([i for i in arr if i < m]) + \
            [i for i in arr if i == m] + \
            quicksort([i for i in arr if i > m])

    vetor = quicksort(vetor)
    return bytes(vetor)


ip = 'localhost'  # Definição do endereço IP
porta = 8000  # Definição da porta de conexão

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Definição do tipo de conexão (TCP ou UDP)
tcp.bind((ip, porta))  # Solicita uma conexão
tcp.listen(1)
print('Servidor: Escutando na porta: {}'.format(porta))

sleep(3)

conexao, cliente = tcp.accept()
print('Servidor: Conexão feita com o cliente: {}'.format(cliente))

sleep(3)

vetor = conexao.recv(1024)
print('Servidor: O vetor foi recebido')

sleep(3)

vetorOrdenado = ordenarVetor(vetor)
print('Servidor: O vetor foi ordenado')

sleep(3)

conexao.send(vetorOrdenado)
print('Servidor: O novo vetor foi enviado')

conexao.close()
