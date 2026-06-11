
def calcular_media (nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))

res = calcular_media(n1, n2)

print(f"Media: {res:.2f}")
