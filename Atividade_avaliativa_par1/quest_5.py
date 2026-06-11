
nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)

print("-"*30)
for nome in nomes:
    print(nome) 