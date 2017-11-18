"""Implementação do cliente utilizando sockets."""
import socket
import random


def criarVetor(tamanho):
    """Função para a criação do vetor."""
    vetor = []
    for i in range(0, tamanho):
        num = random.randint(0, 100)
        if num in vetor:
            pass
        else:
            vetor.append(num)
    print(vetor)
    return bytes(vetor)


ip = 'localhost'  # Definição do endereço IP
porta = 8000  # Definição da porta de conexão

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Definição do tipo de conexão (TCP ou UDP)
tcp.connect((ip, porta))  # Solicita uma conexão
print('Solicitando um a conexão...')

vetor = criarVetor(10)  # Chama a função para criar o vetor e o transformar em um array de bytes
print(vetor)
tcp.send(vetor)  # Envia o vetor em formato de bytes
print('Cliente: Vetor enviado')

print('Cliente: Esperando o novo vetor...')
vetor = tcp.recv(1024)  # Recebe o novo vetor
print('Cliente: O vetor foi recebido')
vetor = list(map(int, vetor))

print('O vetor ordenado é: {}'.format(vetor))  # Mostra o novo vetor

tcp.close()  # Fecha a conexão
