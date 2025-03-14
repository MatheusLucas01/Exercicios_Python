def verifica_letra():
    while True:
        letra = input("Digite uma única letra: ").strip()

        # Verifica se o input tem apenas uma letra
        if len(letra) != 1 or not letra.isalpha(): #--> Retorna se os caracteres são letras
            print("Entrada inválida! Digite Novamente.")
            continue
        
        # Verifica se é vogal ou consoante
        if letra.lower() in "aeiou":
            print(f"{letra} é Vogal")
        else:
            print(f"{letra} é Consoante")
        break

def main():
    verifica_letra()

if __name__ == "__main__":
    main()


# entrada = [int(input(f"Digite a nota {1+i}: ")) for i in range(4)]
# print(entrada)