
nome = input("Digite o nome do aluno: ")

arquivo = open("C:/Users/vboxuser/Documents/alunos.txt", 'a', encoding='utf-8')
arquivo.write(nome + "\n")
arquivo.close()

print("Aluno cadastrado com sucesso")