"""Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que 
o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma 
e a média aritmética. """

numero = int (input("Digite um numero inteiro: "))
soma = 0
media =0
totalN = 0
while numero != 0:
    soma += numero
    totalN += 1
    media = soma / totalN

    numero = int (input("Digite um numero inteiro: "))

print("A quantidade de números digitados foi: ",totalN)
print("A soma de todos os numeros foi: ",soma)
print("A media aritimética entre a quantidade de numeros e a soma é: ",media)