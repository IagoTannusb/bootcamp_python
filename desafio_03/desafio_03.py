#Ajustar o desafio 01 add tratamentos de erros com salario e bonus nao podendo ser menor que 0

nome = input("Digite seu nome: ")
while nome.strip().replace(" ", "").isalpha() == False:
    nome = input("Digite um nome no formato correto: ")

while True:
    try:
        salario = float(input("Digite seu salario mensal: "))
        if salario < 0:
            print("Digite um valor para o salario valido")
        else:
            break
    except ValueError:
        print("Add um salario no formato correto")


while True:
    try:
        bonus = float(input("Informe o bônus que você recebeu: "))
        if bonus < 0:
            print("Digite um bonus valido")
        else:
            break
    except ValueError:
        print("Add o bônus no formato valido")

resultado_final  = 1000 + salario * bonus

print(f"Olá {nome}, o seu bônus foi de {resultado_final}")