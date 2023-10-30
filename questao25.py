# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
number = []

for i in range (0,6):
    insernumer = int(input("digite um número:"))
    if insernumer  % 2 == 0:
        number.append(insernumer)

soma = sum(number)
print(soma)