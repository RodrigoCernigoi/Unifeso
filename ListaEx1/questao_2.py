# Desenvolva um conversor de números romanos para decimais e vice-versa. O programa
# deve lidar com números de 1 a 3999. Implemente funções separadas para cada direção
# de conversão e inclua verificações de entrada válida

def romano_para_decimal(numero_romano):
   
    romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(numero_romano)-1, -1, -1):
        if i == len(numero_romano)-1 or romano[numero_romano[i]] >= romano[numero_romano[i+1]]:
            decimal += romano[numero_romano[i]]
        else:
            decimal -= romano[numero_romano[i]]
    return decimal

def decimal_para_romano(numero_decimal):
   
    if not 1 <= numero_decimal <= 3999:
        raise ValueError("Número decimal fora do intervalo válido (1-3999)")

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    resultado = ''
    i = 0
    while  numero_decimal > 0:
        for _ in range(numero_decimal // valores[i]):
            resultado += romanos[i]
            numero_decimal -= valores[i]
        i += 1
    return resultado

# Verificações de entrada:
try:
    numero_romano = input("Digite um número romano: ")
    print(f"O número decimal equivalente é: {romano_para_decimal(numero_romano)}")
except ValueError as e:
    print(f"Erro: {e}")

try:
    numero_decimal = int(input("Digite um número decimal (1-3999): "))
    print(f"O número romano equivalente é: {decimal_para_romano(numero_decimal)}")
except ValueError as e:
    print(f"Erro: {e}")
