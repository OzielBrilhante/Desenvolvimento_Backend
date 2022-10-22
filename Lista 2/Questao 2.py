"""
Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos.
Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada.
Escrever a média da turma e o resultado da contagem.

"""
notas_alunos = [float]
soma = 0
nota_acima = 0

for i in range(1, 21):
    notas_alunos.append(float(input("Digite a nota do aluno: ")))
    soma += notas_alunos[i]

media = soma/20

for i in range(1, 21):
    if notas_alunos[i] > media:
        nota_acima += 1
    else:
        nota_acima += 0

print(f"\nA media da turma é: {media}, e obtiveram {nota_acima} notas acima da media ")