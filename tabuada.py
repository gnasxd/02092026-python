n = int (input("Digite um valor de 0 a 10: "))
cont = 0
tabu = 0
if n<0 or n>10:
    print("Digite um valor valido!")

while cont<=10:
    print(f"""
{cont}x{n}={cont*n}""")
    cont = cont + 1
