import os
from dataclasses import dataclass

os.system("cls")

# Definindo uma classe.
@dataclass
class Paciente:
    nome: str
    idade: str
    peso: str
    altura: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')



print("\n" + "="*34)
print('= SOLICITANDO DADOS DO PACIENTE =')
print("="*34)

paciente =  Paciente(
    nome= input('Digite seu nome: '),
    idade= input('Digite sua idade: '),
    peso= input('Digite seu peso: '),
    altura= input('Digite sau altura: ')
)

print("\n" + "="*34)
print('= EXIBINDO DADOS DO PACIENTE =')
print("="*34)
paciente.mostrar_dados()