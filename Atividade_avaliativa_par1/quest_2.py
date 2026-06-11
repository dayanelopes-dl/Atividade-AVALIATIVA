

nota1 = float(input("digite a 1º nota: "))
nota2 = float(input("digite a 2º nota: "))
media = (nota1 + nota2) / 2
print(media)

if media >= 7:  
    print("APROVADO")
elif media >= 5:
    print("recuperação")
else:
    print("REPROVADO")
