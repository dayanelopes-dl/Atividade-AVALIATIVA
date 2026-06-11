meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set', 'out', 'nov', 'dez')

print("Digite o mes correspondente ao número, ou 0 para encerrar o programa.")

while True:

    numero = int(input('Digite um número entre 1 e 12: '))
    if numero == 0:
        print("Programa encerrado.")
        break
    elif 1 <= numero <= 12:
        print(f"mes de {meses[numero - 1]}")
