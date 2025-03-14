
def letra_digitada():
    while True:
        sexo = input("Qual o seu sexo? ").strip().lower()
        if sexo == "f":
            print("F - Feminino")
            break
        elif sexo == "m":
            print("M - Masculino")
            break
        else:
            print("Sexo inválido! Tente novamente")
            
def main():
    letra_digitada()

if __name__ == "__main__":
    main()