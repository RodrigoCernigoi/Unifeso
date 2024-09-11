def main() -> None:
   # Escreva um programa em que leia uma sequência de números e exiba a soma deles
   
   num_list = [0]
   num_list.append(int(input("Digite um numero para a Soma: ")))
   option = input("Deseja somar mais algum numero? S/N ")
   while(option == "S"):
       num_list.append(int(input("Digite um numero para a Soma: ")))
       option = input("Deseja somar mais algum numero? S/N ")

   print(sum(num_list))
   
    

if __name__ == "__main__":
    main()


