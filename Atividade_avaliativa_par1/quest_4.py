soma = 0

numero = float(input("Digite um número ou - 0 para sair): "))

while numero != 0:
    soma += numero
    numero = float(input("Digite um número ou - 0 para sair): "))

print(f"Soma dos números: {soma}")