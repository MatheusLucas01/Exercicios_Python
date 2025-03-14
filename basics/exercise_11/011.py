def positivo_ou_negativo():
    while True:
        try:
            valor = float(input("Digite um valor: "))

            if valor > 0:
                print(f"O número {valor} é positivo. ")
                break
            elif valor < 0:
                print(f"O número {valor} é negativo. ")
                break
            else:
                print(None)
                break
        except ValueError:
            print("Isso não é um número, tente novamente!")

def main():
    positivo_ou_negativo()

if __name__ == "__main__":
    main()