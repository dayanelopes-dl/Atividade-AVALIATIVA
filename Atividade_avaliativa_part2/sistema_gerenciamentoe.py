dados_alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    
    if aluno_existe(nome):
        print(f"Erro! O aluno '{nome}' já está cadastrado. Cadastre um novo aluno.")
        return

    try:
        idade = int(input("Digite a idade: "))
        turma = input("Digite a turma: ")
    except ValueError:
        print("Erro! Idade apenas números inteiros !")
        return 
        
    
    dados_alunos.append([nome, 0.0, 0.0, 0.0, 0.0, 0.0, False])
    
    print(f"Aluno {nome} cadastrado com sucesso!")


def aluno_existe(nome):
    
    for i in range(len(dados_alunos)):
        
        if dados_alunos[i][0].lower() == nome.lower():
            return True
    return False


def lancar_notas():
    try:
        if not dados_alunos:
            print("Nenhum aluno cadastrado ainda.")
            return
            
        print("Lista de Alunos:")
        for i in range(len(dados_alunos)):
            print(f"[{i}] - {dados_alunos[i][0]}")
            
        escolha = int(input("Digite o número do aluno para lançar as notas: "))

        if 0 <= escolha < len(dados_alunos):
            
            
            ja_lancado = dados_alunos[escolha][6]
            
            if ja_lancado:
                print(f"Erro! As notas para o aluno {dados_alunos[escolha][0]} já foram cadastradas.")
                return 
                
            print(f"Lançando notas para {dados_alunos[escolha][0]}")
            
            for j in range(4):
                dados_alunos[escolha][1 + j] = float(input(f"Digite a {j+1}ª nota: "))
                
            notas = dados_alunos[escolha][1:5]
            media = sum(notas) / 4

            dados_alunos[escolha][5] = media 
            dados_alunos[escolha][6] = True 
            print("Notas lançadas e médias calculadas com sucesso!")
        
        else:
            print("Aluno inválido.")
     
    except ValueError:
        print("Erro. Apenas valores numéricos são aceitos.")



def situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def consultar_aluno():
    try:
        if not dados_alunos:
            print("Nenhum aluno cadastrado ainda.")
            return

        print("---CONSULTAR ALUNO---")
        for i in range(len(dados_alunos)):
            print(f"[{i}] - {dados_alunos[i][0]}")

        escolha = int(input("Digite o número do aluno para consultar: "))

        if 0 <= escolha < len(dados_alunos):
            aluno = dados_alunos[escolha]
            print(f"Aluno: {aluno[0]}")
            print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}, {aluno[4]}")
            print(f"Média Final: {aluno[5]:.2f}")
    
        else:
            print("Aluno inválido.")
    except:
        print("Erro, apenas numeros inteiros.")

def relatorio_geral():
    if not dados_alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    print("\n--- RELATÓRIO GERAL DOS ALUNOS ---")
    
   
    total_alunos = len(dados_alunos)
    soma_medias = 0.0
    qtd_aprovados = 0
    qtd_recuperacao = 0
    qtd_reprovados = 0
    
   
    nome_melhor = dados_alunos[0][0]
    maior_media = dados_alunos[0][5]
    
    nome_pior = dados_alunos[0][0]
    menor_media = dados_alunos[0][5]

  
    print("-"*40)
    
    for i in range(total_alunos):
        aluno = dados_alunos[i]
        nome = aluno[0]
        media = aluno[5]
        situacao_aluno = situacao(media)
        
        
        print(f"Aluno:{nome} / Notas: ", end="")
        
        
        for j in range(1, 5):
            print(f"[{aluno[j]:.1f}] ", end="")
            
        
        print(f"/ Média: [{media:.2f}] / Situação: {situacao_aluno}")

        
        
        soma_medias += media
        
        
        if situacao_aluno == "Aprovado":
            qtd_aprovados += 1
        elif situacao_aluno == "Recuperação":
            qtd_recuperacao += 1
        else:
            qtd_reprovados += 1
            
        
        if media > maior_media:
            maior_media = media
            nome_melhor = nome
            
        
        if media < menor_media:
            menor_media = media
            nome_pior = nome

   
    media_turma = soma_medias / total_alunos

   
    print("-"*40)
    print(f"Quantidade total de alunos: {total_alunos}")
    print(f"Média geral da turma: {media_turma:.2f}")
    print(f"Melhor aluno: {nome_melhor} (Média: {maior_media:.2f})")
    print(f"Pior aluno: {nome_pior} (Média: {menor_media:.2f})")
    print("-" * 40)
    print(f"Alunos Aprovados: {qtd_aprovados}")
    print(f"Alunos em Recuperação: {qtd_recuperacao}")
    print(f"Alunos Reprovados: {qtd_reprovados}")
    print("-"*40)

def salvar_dados():
    if not dados_alunos:
        print("Não há dados para salvar.")
        return

    try:
        with open("C:/Users/vboxuser/Documents/alunos.txt", "w", encoding="utf-8") as arquivo:
            for aluno in dados_alunos:
                
                linha = f"{aluno[0]};{aluno[1]};{aluno[2]};{aluno[3]};{aluno[4]};{aluno[5]:.2f};{aluno[6]}\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def carregar_dados():
    global dados_alunos
    dados_alunos = [] 
    
    try:
        with open("C:/Users/vboxuser/Documents/alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                
                if linha != "": 
                    dados = linha.split(";")
                    
                    
                    aluno = [
                        dados[0],                  
                        float(dados[1]),           
                        float(dados[2]),           
                        float(dados[3]),           
                        float(dados[4]),           
                        float(dados[5]),           
                        dados[6] == "True"         
                    ]
                    dados_alunos.append(aluno)
                    
        print("Dados dos alunos carregados com sucesso!")
    except FileNotFoundError:
        print("O arquivo ainda não existe. Será criado ao salvar dados.")



def menu_principal():
    while True:
        print("--- SISTEMA DE GERENCIAMENTO ESCOLAR ---")
        print("1 - Cadastrar Aluno")
        print("2 - Lançar Notas")
        print("3 - Consultar Aluno")
        print("4 - Relatório Geral")
        print("5 - Salvar Dados")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            lancar_notas()
        elif opcao == 3:
            consultar_aluno()
        elif opcao == 4:
            relatorio_geral()
        elif opcao == 5:
            salvar_dados()
        elif opcao == 6:
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

carregar_dados()
menu_principal()