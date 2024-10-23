def ContaPalavras(texto):
    palavras = texto.split()  
    return len(palavras)   
    
    
def FuncaoVerificaCandidato (ListFicha):
    for Dicionario in ListFicha:
        Num = Dicionario['Numero']
        if len(Num) > 5:
            return 1
            
        Name = Dicionario['Nome']
        Name = ContaPalavras(Name)
        if Name != 2:
            return 2
            
        Party = Dicionario['Partido']
        if Party == "":
            return 3


def FuncaVerificaEleitor(ListTitulo):
    textopadrao = 'aAbBcDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZçÇ'
    for Dicionario in ListTitulo:
        Nome = Dicionario['Name']
        Nome = ContaPalavras(Nome)
        if Nome != 2:
            return 7
        
        Title = Dicionario['Titulo']
        Title = FormataTitulo(Title)
        if Title != 4:
            for i in textopadrao:
                if Title.find(i) > -1:
                    return 5    
        else:
            return 6
        
        Votado = Dicionario['Voto']
        if Votado.lower() != 'branco':  
            if len(Votado) > 5:
                return 9



        

def VerificarDuplicidadeCandidato(Lista):
    valores_vistos = set()
    duplicados = set()
    for dicionario in Lista:
        for valor in dicionario.values():
            if valor in valores_vistos:
                duplicados.add(valor)
            else:
                valores_vistos.add(valor)
    return duplicados


def VerificarDuplicidadeEleitor(Lista):
    valores_vistos = set()
    duplicados = set()
    for dicionario in Lista:
        for valor in dicionario.values():
            if valor == dicionario['Voto']:
                continue
            else:
                if valor in valores_vistos:
                    duplicados.add(valor)
                else:
                    valores_vistos.add(valor)
    return duplicados


def FormataTitulo (NumTitulo):
    # Remove espaços ou caracteres indesejados
    NumTitulo = NumTitulo.replace(" ", "") 
    
    # Verifica se o texto tem pelo menos 12 caracteres
    if len(NumTitulo) != 12:
        return 4
    
    # Formata no padrão xxxx xxxx xxxx
    return f"{NumTitulo[:4]} {NumTitulo[4:8]} {NumTitulo[8:12]}"

    

#------------Programa principal------------
import time
import sys

Ficha = dict()
ListaCandidatos = list()
Titulo = dict()
ListaTitulo = list()
VotosPorCandidato = dict()
VotosPorCandidatoList = list()

print('')
print('----CADASTRO DE CANDIDATOS----')
print('')
for i in range(0,3):
    Ficha['Nome'] = str(input("Digite seu primeiro e segundo nome: "))
    Ficha['Numero'] = str(input("Digite seu número: "))
    Ficha['Partido'] = str(input("Qual partido você está afiliado: "))
    
    ListaCandidatos.append(Ficha.copy())
    print('')
    if FuncaoVerificaCandidato(ListaCandidatos) == 1:
        print("O tamanho máximo é 5")
        sys.exit()
        break
    if FuncaoVerificaCandidato(ListaCandidatos) == 2:
        print("Informe somente os dois primeiros nomes")
        sys.exit()
        break
    if FuncaoVerificaCandidato(ListaCandidatos) == 3:
        print('É necessario informar seu partido')
        sys.exit()
        break

print('Cadastrando dados...')
time.sleep(3)    

if len(VerificarDuplicidadeCandidato(ListaCandidatos)) != 0: 
    print('Existem dados repetidos')
    sys.exit()

print('')   
print('----ÍNICIO DAS ELEIÇÕES----')
print('')
for i in range(0,10):
    Titulo['Name'] = str(input("Digite seu primeiro e segundo nome: "))
    Titulo['Titulo'] = str(input("Digite o número do seu título de eleitor: "))
    print("CASO DESEJE VOTAR EM BRANCO DIGITE 'branco'")
    Titulo['Voto'] = str(input("Digite o número de quem deseja votar: "))
    
    ListaTitulo.append(Titulo.copy())
    print('')

    if FuncaVerificaEleitor(ListaTitulo) == 6:
        print("O título deve conter exatamente 12 números.")
        sys.exit()
        break
    if FuncaVerificaEleitor(ListaTitulo) == 5:
        print("Apenas são aceitos números no título")
        sys.exit()
        break
    if FuncaVerificaEleitor(ListaTitulo) == 7:
        print("Informe somente os dois primeiros nomes")
        sys.exit()
        break
    if FuncaVerificaEleitor(ListaTitulo) == 9:
        print("O voto deve possuir no máximo 5 números")
        sys.exit()
        break
    
print('Calculando o resultado...')
time.sleep(3)

if len(VerificarDuplicidadeEleitor(ListaTitulo)) != 0: 
    print('Existem dados repetidos') 
    sys.exit()


# FAZ A CONTAGEM DOS VOTOS
QntdVotosBrancos = 0
QntdVotosNulos = 0

# FOR QUE CRIA LISTA COM OS NUMEROS DE CANDIDATOS VALIDOS 
NumValido = dict()
NumValidosss = list()
for dickt in (ListaCandidatos): 
    NumValido['validos'] = dickt['Numero']
    NumValidosss.append(NumValido['validos'])

# FOR QUE COMPARA A LISTA COM OS VOTOS
for RegistroEleitor in (ListaTitulo):
    Vote = RegistroEleitor['Voto']
    if not Vote == 'branco':
        if not Vote in NumValidosss:
            QntdVotosNulos = QntdVotosNulos + 1
    else:
        QntdVotosBrancos = QntdVotosBrancos + 1 

# LISTA CANDIDATOS
for dicio in (ListaCandidatos):  
    democracia = 0
    Brancos = 0

    NumCandidato = dicio['Numero']
    # ANALIZA OS ELEITORES
    for RegistroEleitor in (ListaTitulo):
        Voto = RegistroEleitor['Voto']
        # CASO O VOTO SEJA IGUAL O NUM DO CANDIDATO
        if NumCandidato == Voto:
            democracia = democracia + 1
    VotosPorCandidato['Candidato'] = dicio['Nome']
    VotosPorCandidato['Party'] = dicio['Partido']
    VotosPorCandidato['Votos'] = democracia  
    VotosPorCandidatoList.append(VotosPorCandidato.copy())   

NumVencedor = max(VotosPorCandidato['Votos'] for VotosPorCandidato in VotosPorCandidatoList)
VencedorTrue = [VotosPorCandidato for VotosPorCandidato in VotosPorCandidatoList if VotosPorCandidato['Votos'] == NumVencedor]

if len(VencedorTrue) > 1:
    print('Esses candidatos vão pro segundo turno')
    for DICK in VencedorTrue:
        print(DICK['Candidato'])
        print(DICK['Party'])
    print('')
    print('Votos em branco: ' + str(QntdVotosBrancos))
    print('')
    print('Votos em nulo: ' + str(QntdVotosNulos))
    print('')
else:
    for DICK in VencedorTrue:
        GANHADOR = (DICK['Candidato'])
        PARTIDARIO = (DICK['Party'])
    print('')
    print('PARABÉNS ' + GANHADOR +' DO PARTIDO ' + PARTIDARIO + ' !!! VOCÊ GANHOU AS ELEIÇÕES!!!')
    print('')
    print('Votos em branco: ' + str(QntdVotosBrancos))
    print('')
    print('Votos em nulo: ' + str(QntdVotosNulos))
    print(''
