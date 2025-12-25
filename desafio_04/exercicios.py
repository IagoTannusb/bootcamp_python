# type hint em dict 

from typing import Dict, Any

livro: Dict[str, Any] = {
    "titulo": "O Hobbit",
    "autor": "J.R.R. Tolkien",
    "ano": 1937,
    "preço": 20.30
}


for a, b in livro.items():
    print(f"chave: {a}, valor: {b}")

print("\n")
print("########################")

# Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

lista_emails = list(set(emails))
print(lista_emails)
print("\n")
print("########################")
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]
lista_idade = []
for i in idades:
    if i >= 18:
        lista_idade.append(i)
print(lista_idade)        

print("\n")
print("########################")

# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoas: pessoas["nome"])

print(pessoas_ordenadas)

print("\n")
print("########################")


# Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]

media = sum(numeros) / len(numeros)

print(media)

print("\n")
print("########################")

# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impar = []
par = []
for valor in valores:
    if valor % 2 != 0:
        impar.append(valor)
    else:
        par.append(valor)

print(f"impar: {impar}")
print(f"par: {par}")

print("\n")
print("########################")

# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

produtos[2]["preço"] = 1000
print(produtos)

print("\n")
print("########################")

# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario1_2 = {**dicionario1, **dicionario2}
print(dicionario1_2)
print("\n")
print("########################")

# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

for produto, quantidade in list(estoque.items()):
    if quantidade <= 0:
        estoque.pop(produto)
print(estoque)

print("\n")
print("########################")

# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = []
valores = []

for chave, valor in dicionario.items():
    chaves.append(chave)
    valores.append(valor)

print(chaves)
print(valores)



# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
qtd = {}
for letra in texto:
    if letra in qtd:
        qtd[letra] += 1
    else:
        qtd[letra] = 1

print(qtd)