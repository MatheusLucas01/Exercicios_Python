# Contagem de votos

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A", "E"]

contagem_votos = {}

for produto in votos:
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(f"A quantidade de votos por produto foi de {contagem_votos}")

