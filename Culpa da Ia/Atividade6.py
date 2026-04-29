import os
from dataclasses import dataclass

os.system("cls")

# Definindo uma classe.
@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

print("\n" + "="*34)
print('= SOLICITANDO DADOS DO FORNECEDOR =')
print("="*34)

fornecedor =  Fornecedor(
    nome= input('Digite seu nome: '),
    email= input('Digite sua email: '),
    telefone= input('Digite seu telefone: '),
    endereco= input('Digite sau endereço: ')
)

print("\n" + "="*34)
print('= EXIBINDO DADOS DO FORNECEDOR =')
print("="*34)

print(f'Nome: {fornecedor.nome}')
print(f'Email: {fornecedor.email}')
print(f'Telefone: {fornecedor.telefone}')
print(f'Endereço: {fornecedor.endereco}')

