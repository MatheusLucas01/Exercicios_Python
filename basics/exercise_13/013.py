def calcular_valor(combustivel, preco, litros):
    if litros <= 20:
        desconto = litros * preco * 0.03
    else:
        desconto = litros * preco * 0.05
    valor_total = (litros * preco) - desconto
    return valor_total, desconto

def calcular_abastecimento():
    preco_gasolina = 2.5
    preco_alcool = 1.90

    while True:
        try:
            escolha = int(input("Escolha uma opção: 1 - Gasolina, 2 - Alcool: "))
            if escolha == 1:
                litros = float(input("Quantos litros de gasolina? "))
                if litros <= 0:
                    print("Os valores devem ser positivos.")
                    continue
                valor_gasolina, desconto = calcular_valor('Gasolina', preco_gasolina, litros)
                print(f"Valor total da gasolina com desconto: R${valor_gasolina:.2f}")
                break
            elif escolha == 2:
                litros = float(input("Quantos litros de álcool? "))
                if litros <= 0:
                    print("Os valores devem ser positivos.")
                    continue
                valor_alcool, desconto = calcular_valor('Álcool', preco_alcool, litros)
                print(f"Valor do álcool com desconto: R${valor_alcool:.2f}")
                break
        except ValueError:
            print("Digite apenas números!")

def main():
    calcular_abastecimento()

if __name__ == "__main__":
    main()
