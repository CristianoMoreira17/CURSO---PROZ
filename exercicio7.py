valorp = int(input("Qual e o valor? "))
juros = float(input("Qual e o juros ? "))
anos = int(input ("Quantos anos? "))

montante = valorp + (valorp * juros * anos / 100) 

print ( f"o valor total a ser pago e: {montante:.2f}" )