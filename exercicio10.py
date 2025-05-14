nota1 = int(input("digite o valor da nota1: "))
peso1 = int(input("digite o valor da peso1: "))

nota2 = int(input("digite o valor da nota2: "))
peso2 = int(input("digite o valor da peso2: "))

nota3 = int(input("digite o valor da nota3: "))
peso3 = int(input("digite o valor da peso3: "))

tpeso = peso1 + peso2 + peso3
rt = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / tpeso

print (f"{rt:.2f}")



