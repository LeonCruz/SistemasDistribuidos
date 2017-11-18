"""Implementação do servidor usando sockets."""

import socket


def ordenarVetor(vetorBytes):
    """Função que ordena o vetor."""
    vetor = list(map(int, vetorBytes))

    vetor = quicksort(vetor)

    return bytes(vetor)

def quicksort(arr):
    if len(arr) <= 1: return arr
    m = arr[0]
    return quicksort([i for i in arr if i < m]) + \
        [i for i in arr if i == m] + \
        quicksort([i for i in arr if i > m])


ip = 'localhost'  # Definição do endereço IP
porta = 8000  # Definição da porta de conexão

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Definição do tipo de conexão (TCP ou UDP)
tcp.bind((ip, porta))  # Solicita uma conexão
tcp.listen(1)
print('Servidor: Escutando na porta: {}'.format(porta))

conexao, cliente = tcp.accept()
print('Servidor: Conexão feita com o cliente: {}'.format(cliente))

vetor = conexao.recv(1024)
vetorOrdenado = ordenarVetor(vetor)


conexao.send(vetorOrdenado)


conexao.close()
