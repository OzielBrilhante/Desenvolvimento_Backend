nota1 = float(input("Entre com a primeira nota do aluno: "))
nota2 = float(input("Entre com a segunda nota do aluno: "))

media = float((nota1+nota2)/2)

if 7 <= media <= 10:
    print(f"A media do aluno é: {media}, o aluno está aprovado")
elif 4 <= media < 7:
    print(f"A media do aluno é: {media}, o aluno está na final")
elif media < 0 or media > 10:
    print(f"Média inválida")
else:
    print(f"A media do aluno é: {media}, o aluno está reprovado")
