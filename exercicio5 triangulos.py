

l1 = int(input("Digite o cumprimento do lado 1: "))

l2 = int(input("Digite o cumprimento do lado 2: "))

l3 = int(input("Digite o cumprimento do lado 3: "))

if l1 == l2 == l3:

    print ("E um triângulo equilátero")
    
elif l1 == l2 != l3 or l3 == l2 != l1 or l3 == l1 != l2:
    
    print (" E um triângulo isósceles")

else:
    print (" E um triângulo escaleno")