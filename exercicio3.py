import random 

def main() -> None:
    # Escreva um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador
    # tenta adivinhar. O programa deve dar dicas se o palpite é muito alto ou muito baixo e contar o
    # número de tentativas.
    
    numPlayer = int(input("Digite um número aleatório de 1 a 100: "))
    randomNum = random.randrange(0,100)
    while(numPlayer != randomNum):
       
        if(numPlayer > randomNum):
            print("Tente um numero menor")
    
        if(numPlayer < randomNum):
            print("Tente um numero maior")
        
        numPlayer = int(input())
        
       
    print("Você acertou!")
    
    # print(f"O número correto é:{randomNum}")

if __name__ == "__main__":
    main()


