senha = int(input("advinhe um numero de 1 a 10: "))
 

while senha != 5:
        if senha > 5 or senha < 10: 
          print("numero incorreto, é um numero menor") 
          senha = int(input("advinhe um numero: "))
        elif senha > 10:
             print("esse numero não esta entre 1 e 10")  
             senha = int(input("advinhe um numero: "))    
        elif senha < 5:
             print("numero incorreto, é um numero maior") 
             senha = int(input("advinhe um numero: "))
print("numero correto")
     

