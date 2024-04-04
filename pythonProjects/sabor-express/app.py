# Realizando importacoes

import os


def exibir_programa():
    # Print - sout
    print("Restaurante")

    print('1. Cadastrar resturante')
    print('2. Listar resturante')
    print('3. Ativar resturante')
    print('4. Sair')

def escolher_opcao():
    # Interagir com usuario - Scanner
    # Ao utilizar o input, salva o resultado na variavel como string.
    # Transformamos a variavel em inteiro
    opcao = int(input('Escolha uma opção: '))
    # print(type(opcao))


    # Para concatenar uma variavel com string - Interpolação

    # print(f'Voce escolheu a opção: {opcao}')
    if (opcao == 1):
        print('opcao 1')
    elif (opcao == 2):
        print('opcao 2')
    elif (opcao == 3):
        print('opcao 3')
    else:
        finalizar_app()

# Criar uma função

def finalizar_app():
    os.system('cls')
    print('Finalizando o programa')

def main():
    exibir_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()


