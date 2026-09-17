""" Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança. Exiba os 
valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período."""
"""Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor 
será depositado no inicio de cada mês, e você deve considera-lo para o calculo de juros do mês seguinte"""


saldoInicial = int (input("Qual será o deposito inicial na poupança?"))
taxa = 0.005
meses = 0
saldo = 0
deposito = 400
while meses <= 24:  
    print(f"{saldo}")
    if meses >= 1:
     saldo = saldo* (1 + taxa)
    
    saldo = saldo + deposito
    print(f"saldo do mes que vem = {saldo}")
    meses = meses + 1
