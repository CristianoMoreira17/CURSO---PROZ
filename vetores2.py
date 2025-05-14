alunos = []

for i in range(5):


    nome = input("Digite o nome do aluno: ")
    av1 = float(input("Digite a nota da AV1: ")) 
    av2 = float(input("Digite a nota da AV2: ")) 

    media = (av1 + av2) / 2

    aluno = {
        "nome":nome,
        "av1": av1,
        "av2": av2,
        "media": media
    }

    alunos.append(aluno)

print("\n--- Resultado Final ---\n")
print(f"{aluno['nome']} - AV1: {aluno['av1']:.2f} | AV2: {aluno['av2']:.2f} | Média: {aluno['media']:.2f}")