## Programa que calcula metros para centímentros 
def metros_para_centimetros():
    while True:
        try:
            metros = float(input("Digite o tamanho em metros para saber os centimetros: "))
            centimetros = metros * 100
            print(f"O valor em centimentros de {metros:.0f} metros, é de {centimetros:.0f} centimetros! ")
            break
        except ValueError:
            print("Digite apenas números!")


def main():
    metros_para_centimetros()


if __name__ == "__main__":
    main()