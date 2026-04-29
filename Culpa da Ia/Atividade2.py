import os
from dataclasses import dataclass

os.system("cls")

# Definindo uma classe.
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

cliente1 = Cliente('Maria', 'maria@gmail.com', ' 71 99287-9473')

@dataclass
class Funcionario:
    nome: str
    matricula: str
    email: str
    setor: str

Funcionario1 = Funcionario('Maria', '30346982', 'maria@gmail.com', 'Recursos Humanos' )

print("\n" + "="*45)
print(f'Nome: {cliente1.nome}')
print(f'E-mail: {cliente1.email}')
print(f'Telefone: {cliente1.telefone}')

print("\n" + "="*45)
print(f'Nome: {Funcionario1.nome}')
print(f'Matricula: {Funcionario1.matricula}')
print(f'E-mail: {Funcionario1.email}')
print(f'Setor: {Funcionario1.setor}')
