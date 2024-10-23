# Neste problema, você terá acesso aos registros de banco de dados referentes ao acervo
# de livros e membros de uma biblioteca pertencente à uma instituição de ensino. Cada
# livro é composto por um título, lista de autores, edição, e quantidade de exemplares
# disponíveis na biblioteca. Implemente as funcionalidades de locação e entrega de
# exemplares do programa. Atente-se que, durante o processo de locação, é registrado a
# matrícula do membro da biblioteca que está alocando o livro, o dia da locação e o dia da
# devolução, 15 dias corridos após a data de locação. Já no processo de devolução,
# implemente as funcionalidades de verificação do título do livro devolvido, existência de
# atraso e a reposição das quantidades alocadas. Caso haja atraso na entrega, o membro
# deverá ser multado em R$ 10,00 por dia de atraso. Membros não pertencentes à
# instituição não podem alocar livros. Por fim, dê a opção do usuário do sistema informar
# uma data de início e fim para obter um relatório das alocações, devoluções, quantidades
# de atrasos e o total em reais pago em multas por cada membro.
import datetime
import csv

def carregar_dados(arquivo_livros, arquivo_membros):
    livros = []
    membros = []

    with open(arquivo_livros, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            livros.append(row)

    with open(arquivo_membros, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            membros.append(row)

    return livros, membros

# Chamar a função para carregar os dados
livros, membros = carregar_dados('livros.csv', 'membros.csv')

locacoes = [
    
    # teste de locacao
]

def menu():
    print("1. Realizar locação")
    print("2. Realizar devolução")
    print("3. Gerar relatório")
    print("4. Sair")

def locar_livro(livro, membro, data_locacao):
    for livro_info in livros:
        if livro_info["titulo"] == livro:
            for membro_info in membros:
                if membro_info["matricula"] == membro:
                    print("Membro não pertence à instituição.")
                    return
            if livro_info["quantidade"] == 0:
                print("Não há exemplares disponíveis deste livro.")
                return

            locacoes.append({
                "livro": livro,
                "membro": membro,
                "data_locacao": data_locacao,
                "data_devolucao": (datetime.datetime.strptime(data_locacao, "%Y-%m-%d") + datetime.timedelta(days=15)).strftime("%Y-%m-%d"),
                "devolvido": 0,
                "atrasos": 0,
                "multa": 0
            })
            livro_info["quantidade"] -= 1
            print("Livro locado com sucesso!")
            return 

    print("Livro não encontrado.")
def devolver_livro(livro, membro, data_devolucao):
    for locacao in locacoes:
        if locacao["livro"] == livro and locacao["devolvido"] == 0 and locacao["membro"] == membro:
            locacao["devolvido"] = 1
            data_devolucao_esperada = locacao["data_devolucao"]
            if data_devolucao > data_devolucao_esperada:
                dias_atraso = (datetime.datetime.strptime(data_devolucao, "%Y-%m-%d") - datetime.datetime.strptime(data_devolucao_esperada, "%Y-%m-%d")).days
                multa = dias_atraso * 10
                locacao["multa"] = multa
                locacao["atrasos"] += 1;
                print(f"Livro devolvido com {dias_atraso} dias de atraso. Multa de R$ {multa:.2f}.")
                
            else:
                print("Livro devolvido com sucesso.")
            
            for livro_info in livros:
                if livro_info["titulo"] == livro:
                    livro_info["quantidade"] += 1
                    break
            return
    print("Locação não encontrada.")

def gerar_relatorio(data_inicio, data_fim):
    data_inicio = datetime.datetime.strptime(data_inicio, "%Y-%m-%d")
    data_fim = datetime.datetime.strptime(data_fim, "%Y-%m-%d")
    

    relatorio = {}
    
    
    for locacao in locacoes:
        
        
        data_loc = datetime.datetime.strptime(locacao["data_locacao"], "%Y-%m-%d")
        if data_inicio <= data_loc <= data_fim:
            membro = locacao["membro"]

            if membro not in relatorio:
                relatorio[membro] = {
                    "locacoes": 1,
                    "devolucoes": int(locacao["devolvido"]),
                    "atrasos": int(locacao["atrasos"]),
                    "multa": float(locacao["multa"])
                }
            else:
                
                relatorio[membro]["locacoes"] += 1
                relatorio[membro]["devolucoes"] += int(locacao["devolvido"])
                relatorio[membro]["atrasos"] += int(locacao["atrasos"])
                relatorio[membro]["multa"] += float(locacao["multa"]) 
                
    

    # Cabeçalho do relatório
    print("Relatório de Locações")
    print("-------------------------------------------------------")
    print("Membro   | Locações | Devoluções | Atrasos | Multa     ")
    print("---------|----------|------------|---------|-----------")

    
    for membro, dados in relatorio.items():
        print(f"{membro:7} | {dados['locacoes']:10} | {dados['devolucoes']:11} | {dados['atrasos']:7} | R$ {dados['multa']:5.2f}")

    print("-------------------------------------------------------")
while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        livro = input("Digite o título do livro: ")
        membro = input("Digite a matrícula do membro: ")
        data_locacao = input("Digite a data da locação (YYYY-MM-DD): ")
        locar_livro(livro, membro, data_locacao)
    elif opcao == 2:
        livro = input("Digite o título do livro: ")
        membro = input("Digite a matrícula do membro: ")
        data_devolucao = input("Digite a data da devolução (YYYY-MM-DD): ")
        devolver_livro(livro, membro, data_devolucao)
    elif opcao == 3:
        data_inicio = input("Digite a data de início do relatório (YYYY-MM-DD): ")
        data_fim = input("Digite a data de fim do relatório (YYYY-MM-DD): ")
        gerar_relatorio(data_inicio, data_fim)
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")
