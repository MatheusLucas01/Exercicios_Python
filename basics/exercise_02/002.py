# Contas de matemática

print("--- Contas de Matemática ---")

while True:
    try:
        entrada1 = float(input("Digite um número inteiro: "))
        entrada2 = float(input("Digite outro número inteiro: "))
        entrada3 = float(input("Digite um número real: "))
        break
    except ValueError:
        print("Digite apenas números.")


produto1 = entrada1 * 2 + entrada2 / 2
produto2 = entrada1 * 3 + entrada3
produto3 = entrada3**3
print()
print(f"O produto do dobro do primeiro número informado com metade do segundo é = {produto1}")
print(f"A soma do triplo do primeiro número informado com o terceiro é = {produto2}")
print(f"O terceiro número informado elevado ao cubo é = {produto3} ")
        
lista1 =[entrada1, entrada2, entrada3]
print("Os números informados foram", lista1)