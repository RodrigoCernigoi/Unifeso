# Selecionar uma palavra aleatoria de uma lista ja estabelacida

# Deve oferecer três chances para o usuário adivinhar a palavra

# Entre tentativas é preciso informar quais letras o usuário acertou

# Dizer se a letra está na posição certa ou errada

#Funções
def AttempsLeft(E):
    txt = ''
    if E == 2:
        txt = 'segunda'
    if E == 3:
        txt = 'última'
    if E == 6:
        txt = '2'
    if E == 7:
        txt = '1'
    return txt


def FuncaoLetradaComplexa(txtUsuario,txtCerto):
    i = 0
    for L in txtUsuario:
        #Verifico se a letra existe na lista
        if L in txtCerto:
            if txtCerto[i] == txtUsuario[i]:
                print("Letra na posição certa: ",L, i+1)
            else:
                c = i
                for c in range(i,len(txtCerto)):
                    if txtCerto[c] == L:
                        print("Posição correta da letra " + L.upper() + " na palavra chave: " ,c+1)
        i = i+1
#Programa principal
import random
PalavrasChave = ['laranja', 'uva', 'manga', 'pera', 'morango', 'banana', 'kiwi' ,'abacate', 'abacaxi', 'cereja']
PalavraEscolhida = random.choice(PalavrasChave)

print('Você possui três tentativas. Acentos não são contablizados')
print('!!!Não digite nomes com numero de letras maior que o informado!!!')
print('')
PalavraUsuaria = input('Digite o nome de uma fruta com ' + str(len(PalavraEscolhida)) + ' letras: ')
PalavraUsuaria = PalavraUsuaria.lower()
print(PalavraUsuaria)
for i in range(1,4):
    if len(PalavraUsuaria) <= len(PalavraEscolhida):
        if PalavraUsuaria == PalavraEscolhida:
            if i == 1:
                print('Parabéns, você acertou a palavra na primeira tentativa')
                break
                
            print('Parabéns, você acertou a palavra na ' + str(AttempsLeft(i)) + ' tentativa')
            break
        elif i == 3:
            print('Não foi dessa vez :(')
            break
        else:    
            print('Você errou e tem apenas '+str(AttempsLeft(i+5))+' tentativas.')
            FuncaoLetradaComplexa(PalavraUsuaria,PalavraEscolhida)
        i - 1
        print("")
        PalavraUsuaria = input('Digite outra palavra: ')
        print("")
        PalavraUsuaria = PalavraUsuaria.lower()
    else:
        print('Eu disse nada de número maior que o informado >:(')
        break
