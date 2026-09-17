""" Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte tambem o 
valor mensal que sera pago. Imprima o numero de meses para que a divida seja paga, o total pago e o total 
 de juros pago."""

valorInicial = float (input("Qual o valor inicial da divida? "))
jurosMensal = float (input("Qual o valor do juros mensal? "))
parcelaMensal = float (input("Qual o valor das parcelas? " ))
cont = 1
jurosTotal = 0
valorPago = 0
valorTotal = 0
meses = valorInicial/parcelaMensal
while cont <=meses :
    somaJuros = parcelaMensal + (jurosMensal*cont)/100
    jurosTotal = somaJuros + jurosTotal

    valorPago = somaJuros + parcelaMensal
    valorTotal += valorPago
    cont += 1
print(f"A quantidade de meses a pagar é de {meses} meses")
print(f"O total a pago é {valorTotal}, e o juros total pago foi: {jurosTotal}") 