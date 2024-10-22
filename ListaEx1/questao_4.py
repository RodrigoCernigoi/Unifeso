# Desenvolva um programa que simule um caixa eletrônico de um banco com múltiplas
# contas correntes. O programa deve permitir operações como depósito, saque,
# transferência entre contas e consulta de extrato (o extrato deve exibir o saldo da conta,
# juntamente com o registro de todas as transações efetuadas pelo cliente). Implemente
# também um sistema de cadastro de senhas para cada nova conta cadastrada. Essa
# senha será requerida pelo sistema ao usuário para a conclusão de uma das transações
# supracitadas. No caso do usuário digitar três vezes a senha incorreta, a conta do usuário
# deverá ser bloqueada e uma mensagem deverá surgir, orientando que o cliente se dirija
# à boca do caixa para efetuar o desbloqueio

contas = {}


def cadastrar_conta():
    numero_conta = int(input("Digite o número da conta: "))
    senha = input("Digite a senha: ")
    deposito_inicial = float(input("Digite o valor do depósito inicial: "))

    contas[numero_conta] = {
        "saldo": deposito_inicial,
        "senha": senha,
        "extrato": []
    }
    print("Conta cadastrada com sucesso!")

def verificar_senha(numero_conta, senha):
    if numero_conta in contas:
        if contas[numero_conta]["senha"] == senha:
            return True
        else:
            return False
    else:
        print("Conta não encontrada.")
        return False

def depositar(numero_conta, valor):
    if verificar_senha(numero_conta, input("Digite a senha: ")):
        contas[numero_conta]["saldo"] += valor
        contas[numero_conta]["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Senha incorreta.")

def sacar(numero_conta, valor):
    if verificar_senha(numero_conta, input("Digite a senha: ")):
        if contas[numero_conta]["saldo"] >= valor:
            contas[numero_conta]["saldo"] -= valor
            contas[numero_conta]["extrato"].append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Senha incorreta.")
        
def transferir(numero_conta_origem, numero_conta_destino, valor):
    if verificar_senha(numero_conta_origem, input("Digite a senha: ")):
        if contas[numero_conta_origem]["saldo"] >= valor:
            contas[numero_conta_origem]["saldo"] -= valor
            contas[numero_conta_destino]["saldo"] += valor
            contas[numero_conta_origem]["extrato"].append(f"Transferência: R$ {valor:.2f} para {numero_conta_destino}")
            contas[numero_conta_destino]["extrato"].append(f"Recebido: R$ {valor:.2f} de {numero_conta_origem}")
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Senha incorreta.")
        
def extrato(numero_conta):
    if verificar_senha(numero_conta, input("Digite a senha: ")):
        print("\nExtrato Bancário")
        print("Número da conta:", numero_conta)
        for transacao in contas[numero_conta]["extrato"]:
            print(transacao)
        print(f"Saldo atual: R$ {contas[numero_conta]['saldo']:.2f}")
    else:
        print("Senha incorreta.")

def verificar_senha(numero_conta, senha, tentativas=0):
    if numero_conta in contas:
        if contas[numero_conta]["senha"] == senha:
            return True
        else:
            tentativas += 1
            if tentativas == 3:
                contas[numero_conta]["bloqueado"] = True
                print("Conta bloqueada. Dirija-se à agência para desbloqueio.")
            else:
                print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")
            return False
    else:
        print("Conta não encontrada.")
        return False

def menu():
    while True:
        print("\n--- Caixa Eletrônico ---")
        print("1. Cadastrar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Extrato")
        print("6. Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrar_conta()
        elif opcao == 2:
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser depositado: "))
            depositar(numero_conta, valor)
        elif opcao == 3:
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser sacado: "))
            sacar(numero_conta, valor)
        elif opcao == 4:
            numero_conta_origem = int(input("Digite o número da conta de origem: "))
            numero_conta_destino = int(input("Digite o número da conta de destino: "))
            valor = float(input("Digite o valor a ser transferido: "))
            transferir(numero_conta_origem, numero_conta_destino, valor)
        elif opcao == 5:
            numero_conta = int(input("Digite o número da conta: "))
            extrato(numero_conta)
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
