# n  = int(input("Digite um número: "))

# eh_primo = True
# if  n < 2:
#    eh_primo = True
# else:
#    divisor=2
#    while divisor * divisor <= n:
#     if n % divisor == 0:
#       eh_primo = False
#       break
#     divisor += 1
# if eh_primo:
#   print(f'{n} é primo!')
# else:
#      print(f'{n} não é primo.')   

n  = int(input("Digite um número: "))
eh_primo = True
if  n < 2:
    eh_primo = True
else:
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break
if eh_primo:      
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo.')   