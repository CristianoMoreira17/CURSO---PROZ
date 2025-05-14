valor = int(input("Qual valor do produto? "))
desc = float(input("Quanto esse produto do desconto? "))

rt =  valor * desc / 100


rt2 = valor - rt

print  (f"{rt2:.2f}")