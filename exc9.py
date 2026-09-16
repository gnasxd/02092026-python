n1 = float (input("Digite o primeiro valor: "))
n2 = float (input("Digite o segundo valor: "))
cont = 0
div = n1 / n2
print (f"o resultado da divisao dos dois numeros é {div}")
while n1 >= n2:
    n1 -= n2
    cont+= 1
print(f"{n2} - {n2} - {n2} - {n2} - {n2} = {cont}")
print(f"o resto da divisão é {n1}")