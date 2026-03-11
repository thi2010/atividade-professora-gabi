aluno = {}

aluno["nome"] = input("Nome do aluno: ")
aluno["nota1"] = float(input("Nota 1: "))
aluno["nota2"] = float(input("Nota 2: "))

aluno["media"] = (aluno["nota1"] + aluno["nota2"]) / 2

print("Dados do aluno:", aluno)

if aluno["media"] >= 7:
    print("Situação: Aprovado")
elif aluno["media"] >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")