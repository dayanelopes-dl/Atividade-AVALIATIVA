

matriz = []

soma = 0 

for i in range(3):
    linha = [] 
    for j in range(3): 
        msg = f'digite valores da matriz 3x3 [{i}][{j}]: '
        linha.append(int(input(msg))) 
    matriz.append(linha) 

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[1])):
        soma = soma + matriz[i][j]  

print(f"A soma de todos os elementos: {soma}")

print(f"valores em diagonal principal : {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")

