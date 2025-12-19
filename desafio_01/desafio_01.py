nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario mensal: "))
bonus = float(input("Informe o bônus que você recebeu: "))

resultado_final  = 1000 + salario * bonus

print(f"Olá {nome}, o seu bônus foi de {resultado_final}")

