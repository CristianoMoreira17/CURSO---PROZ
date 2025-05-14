valor = int(input("Qual valor do produto? "))


if valor< 100:

    print ("o valor não tera desconto.")

else:
     desc = float(input("Quanto sera o desconto?  %"))

     rt =  valor * desc / 100


     rt2 = valor - rt

     print  ("o valor do produto com desconto sera R$"f"{rt2:.2f}")