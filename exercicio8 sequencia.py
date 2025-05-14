# n = int(input("Digite até qual número você quer ver na sequência de Fibonacci:  "))
# a, b =0, 1
# print ("sequencia de fi")
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b

n = int(input("Quantos numeros da sequencia quer ver? "))
a, b = 0, 1
for i in range(n): 
   print (a, end=" ") 
   a, b = b, a + b