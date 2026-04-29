import os
from dataclasses import dataclass

os.system("cls")

# Definindo uma classe.
@dataclass
class Cliente:
    nome: str
    email: str

cliente1 = Cliente('Maria', 'maria@gmail.com')

print(f'Nome: {cliente1.nome}')
print(f'E-mail: {cliente1.email}')