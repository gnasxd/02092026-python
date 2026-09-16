num1 = int (input("Digite um valor: "))
num2= int (input("Digite o segundo valor: "))
res = 0
cont = 0
res2 = 0
cont2 = 0
mult = num1 * num2

print(f"O valor da multiplicação é {mult}")

while cont<num1:
    res += num2
    cont += 1

    
print(f"{num2} + {num2} + {num2} + {num2} = {res}")

while cont2<num2:
    res2 += num1
    cont2 += 1


print(f"{num1} + {num1} + {num1} + {num1} + {num1} = {res2}")



