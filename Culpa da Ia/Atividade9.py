import os
from dataclasses import dataclass

os.system("cls")

# Definindo uma classe.
@dataclass
class Endereco:
    logradouro: str
    numero: str


# Definindo uma classe.
@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')

print('= Solicitando dados do cliente =')
cliente =  Cliente(
    nome= input('Digite seu nome: '),
    idade= int(input('Digite sua idade: ')),
    endereco= Endereco(
        logradouro= input('Digite seu endereço: '),
        numero= input('Digite o número: ')
    )
)

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()
