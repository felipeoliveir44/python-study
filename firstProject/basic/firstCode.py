# Exemplo de variáveis e tipos de dados
nome = "João"
idade = 30
altura = 1.75
é_estudante = True

print(nome)
print(idade)
print(altura)
print(é_estudante)

# Exemplo de condicionais
nota = 7.5

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Exemplo de loops
print("Utilizando For")
# Loop for
for i in range(5):  # Imprime números de 0 a 4
    print(i)
print("----------------------------")

# Loop while
print("Utilizando while")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
print("----------------------------")

# Exemplo de listas e dicionários
# Lista
frutas = ['maçã', 'banana', 'laranja']
print(frutas[0])  # Imprime 'maçã'

# Dicionário
aluno = {'nome': 'Maria', 'idade': 25, 'curso': 'Engenharia'}
print(aluno['idade'])  # Imprime 25

# Exemplo de função
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ana")  # Chama a função e imprime "Olá, Ana!"