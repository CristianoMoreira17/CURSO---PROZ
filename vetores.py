comissoes = []

for i in range(1):
    nome = input("Digite o nome do funcionário: ")
    comissaoum = float(input("Digite a comissão do primeiro mês: "))
    comissaodois = float(input("Digite a comissão do segundo mês: "))

    media = (comissaoum + comissaodois) / 2

    comissoes.append({
        "nome": nome,
        "comissao 1": comissaoum,
        "comissao 2": comissaodois,
        "media": media
    })

print("\n--- Resultado Final ---")

for comissao in comissoes:
     print(f"{comissao['nome']} - comissão 1: {comissao['comissao 1']} | comissão 2:{comissao['comissao 2']} | média: {comissao['media']:.2f}")