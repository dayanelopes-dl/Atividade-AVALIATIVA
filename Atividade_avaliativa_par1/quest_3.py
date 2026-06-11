
soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))
    soma += numero

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")