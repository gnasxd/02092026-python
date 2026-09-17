
res = int(input("""Deseja começar a comprar? 
[0] não
[1] sim\n"""))
print()
somaTotal = 0
while res != 0:
   codigo = int (input("""Por favor, insira o codigo do produto:
    Código 1 - preço R$ 0,50
    Código 2 - preço R$ 1,00
    Código 4 - preço R$ 4,00
    Código 5 - preço R$ 7,00
    Código 9 - preço R$ 8,00\n"""))
   print()
   quantidade = int (input("Qual a quantidade que deseja comprar?\n "))
   print ()
   res = int (input("""Deseja continuar comprando? 
    [0] não
    [1] sim\n"""))
   print()
   match codigo:
            case 1:
                totalCompras = 0.50 * quantidade
            case 2:
                totalCompras = 1 * quantidade
            case 4:
                totalCompras = 4 * quantidade
            case 5:
                totalCompras = 7 * quantidade
            case 9:
                totalCompras = 8 * quantidade
            case _:
                totalCompras = 0
                print("Digite um codigo válido.")
   somaTotal += totalCompras
print("O total de compras ficou no valor de: ",somaTotal,"R$")
    