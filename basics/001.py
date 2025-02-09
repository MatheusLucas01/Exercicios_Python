print("--- Número informado ---")

while True:

    try:
        numero = input("Digite um número: ")
        numero = float(numero)
        break
    except:
        print("Digite apenas números.")


print(f"O número informado foi {numero}")