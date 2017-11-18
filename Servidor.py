"""Implementação do servidor usando sockets."""
import socket


def ordenarVetor(vetorCliente):
    """Função para ordenar o vetor."""
    return vetorCliente


ip = 'localhost'  # Definição do endereço IP
porta = 5000   # Definição da porta de conexão

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Definição do tipo de conexão (TCP ou UDP)
tcp.bind((ip, porta))  # Define para qual endereço o servidor ira aguardar uma conexão
tcp.listen(1)  # Define o limite de conexões

print('Servidor: Escutando na porta: {}'.format(porta))  # Informa a porta que está escutando

conexao, cliente = tcp.accept()  # Aceita uma conexão
print('Servidor: Conexão aceita com o cliente: {}'.format(cliente))

vetorCliente = conexao.recv(1024)  # Recebe o vetor
print('Servidor: Vetor recebido')
print(vetorCliente)
vetorOrdenado = ordenarVetor(vetorCliente)  # Chama a função para ordenar o vetor e o transformar em um array de bytes
print(vetorOrdenado)
print('Servidor: O vetor foi ordenado')

print('O vetor ordenado é {}'.format(vetorOrdenado))

conexao.send(vetorOrdenado)
print('Servidor: O vetor foi reenviado')

conexao.close()  # Fecha a conexão
