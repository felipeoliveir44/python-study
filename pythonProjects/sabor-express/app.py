# Realizando importacoes

import os

restaurantes = []

def exibir_programa():
    # Print - sout
    print("Restaurante")

    print('1. Cadastrar resturante')
    print('2. Listar resturante')
    print('3. Ativar resturante')
    print('4. Sair')

def opcao_invalida():
    print('Opção invalida!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    # Adicionar a lista
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado! ')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def listar_restaurante():
    os.system('cls')
    print("Lista de restaurantes:")
    for item in restaurantes:
        print("- " + item)
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        # Interagir com usuario - Scanner
        # Ao utilizar o input, salva o resultado na variavel como string.
        # Transformamos a variavel em inteiro
        opcao = int(input('Escolha uma opção: '))
        # print(type(opcao))
        # Para concatenar uma variavel com string - Interpolação
        # print(f'Voce escolheu a opção: {opcao}')
        if (opcao == 1):
            cadastrar_restaurante()
        elif (opcao == 2):
            listar_restaurante()
        elif (opcao == 3):
            print('opcao 3')
        else:
            finalizar_app()
    except:
        opcao_invalida()


# Criar uma função

def finalizar_app():
    os.system('cls')
    print('Finalizando o programa')

def main():
    os.system('cls')
    exibir_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()


