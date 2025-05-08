''' Criado um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do
Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n'), incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. '''


def leiaInt(número):
    while True:
        try:
            n = int(input(número))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(número):
    while True:
        try:
            n = float(input(número))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Por favor, digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')

