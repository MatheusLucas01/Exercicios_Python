# Número informado

print("--- Número informado ---")

while True:
    try: 
        entrada = input("Digite um número: ")
        numero = float(entrada)
        break
    except:
        print(f"{entrada} não é um número, digite apenas números!")


print(f"O número informado foi {numero:.2f}")