# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Escolha um numero: '))

if(numero % 2 == 0):
    print(f'O numero {numero} é par!')
else:
    print(f'O numero {numero} é impar!')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias

idade = int(input('Qual a sua idade? '))

if idade <= 12:
    print('Criança')
elif 13 <= idade <= 18:  # Correção na condição de idade entre 13 e 18
    print('Adolescente')
else:
    print('Adulto')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

userSalvo = str(input('Digite seu nome de usuário: '))
senhaSalva = str(input('Digite sua senha: '))

userInformado = str(input('Digite seu nome de usuário: '))
senhaInformada = str(input('Digite sua senha: '))

if userSalvo == userInformado and senhaSalva == senhaInformada:
    print('Usuário logado!')
else:
    print('Usuário ou senha incorretos! Tente novamente.')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")