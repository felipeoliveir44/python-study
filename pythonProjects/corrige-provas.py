
gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'C', 'A', 'B', 'E']
respostasAluno = ['A', 'C', 'B', 'A', 'E', 'C', 'A', 'A', 'D', 'B']
indices_acertos = []
acertos = 0

for i in range(len(gabarito)):
    if(gabarito[i] == respostasAluno[i]):
        acertos += 1
        indices_acertos.append(i + 1)

print(f'Número de acertos: {acertos}')
print(f'Índices das questões corretas: {indices_acertos}')

if(acertos <= 5):
    print("Voce está reprovado!")
else:
    print("Voce está aprovado!")

