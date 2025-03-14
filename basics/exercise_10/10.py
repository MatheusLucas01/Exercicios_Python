def nota():

    while True:
        try:
            nota = int(input("Digite uma nota entre 0 e 10: "))
            if nota > 0 and nota < 10:
                print(f"A nota digitada foi {nota}")
                break
            else:
                print("Nota inválida.")
                continue

        except ValueError:
            print("Nota inválida! Tente novamente.")

def main():
    nota()

if __name__ == "__main__":
    main()