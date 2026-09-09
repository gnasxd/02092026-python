n = int (input("digite um numero: "))
cont = int (input("por qual numero de 0 a 10 deseja começar a tabuada? "))
n2 = int (input("qual numero de 0 a 10 você deseja finalizar a tabuada? "))

while cont <=n2:
    print(f"""{cont}x{n}={cont*n}""")
    cont= cont + 1
    