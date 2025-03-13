## Programa que calcula metros para centímentros 

def metros_para_centimetros():
    while True:
        try:
            metros = float(input("Digite o tamanho em metros para saber os centimetros: "))
            centimetros = metros * 100
            print(f"O valor em centímentros de {metros:.2f} metros, é de {centimetros:.0f} centímetros! ")
            break
        except ValueError:
            print("Digite apenas números!")


def main():
    metros_para_centimetros()


if __name__ == "__main__":
    main()