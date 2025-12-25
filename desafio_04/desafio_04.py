# Refatorando o código anterior com os aprendizados da aula 

def solicitar_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Erro: Digite um valor positivo.")
            else: 
                return valor
        except ValueError:
            print("Erro: Digite número válido.")

def calcular_kpi(salario: float, bonus: float) -> float:
    constante = 1000
    return constante + salario * bonus


nome_usuario = input("Digite seu nome: ")
while not nome_usuario.strip().replace(" ", "").isalpha():
    nome_usuario = input("Nome inválido. Digite apenas letras: ")

salario_usuario = solicitar_valor("Digite seu salario mensal: ")
bonus_usuario = solicitar_valor("Digite o bônus recebido: ")

valor_bonus = calcular_kpi(salario_usuario, bonus_usuario)

info_funcionario = {
    "nome": nome_usuario,
    "salario_base":salario_usuario,
    "kpi_calculado": valor_bonus
}

print(f"Olá {info_funcionario["nome"]}, o seu bônus foi de {info_funcionario["kpi_calculado"]}")