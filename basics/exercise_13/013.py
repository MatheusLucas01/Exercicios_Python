def calcular_valor_combustivel(litros, preco_litro):
    if litros <= 0:
        print("Quantidade de litros deve ser maior que zero!")
        return None, None

    if litros <= 20:
        desconto = litros * preco_litro * 0.03
    else:
        desconto = litros * preco_litro * 0.05

    valor_total = (litros * preco_litro) - desconto
    return valor_total, desconto

def abastecer_gasolina():
    preco_gasolina = 2.5
    while True:
        try:
            litros = float(input("Quantos litros de gasolina? "))
            total, desconto = calcular_valor_combustivel(litros, preco_gasolina)
            if total is not None: # Se o total não for None
                print(f"\nValor da gasolina: R${total:.2f}")
                print(f"Você teve um desconto de R${desconto:.2f}")
                break
        except ValueError:
            print("Digite um número válido para a quantidade de litros.")

def abastecer_alcool():
    preco_alcool = 1.90
    while True:
        try:
            litros = float(input("Quantos litros de álcool? "))
            total, desconto = calcular_valor_combustivel(litros, preco_alcool)
            if total is not None:
                print(f"\nValor do álcool: R${total:.2f}")
                print(f"Você teve um desconto de R${desconto:.2f}")
                break
        except ValueError:
            print("Digite um número válido para a quantidade de litros.")

def calcular_abastecimento():
    while True:
        try:
            escolha = int(input("Escolha uma opção: 1 - Gasolina, 2 - Álcool: "))

            if escolha == 1:
                abastecer_gasolina()
                break
            elif escolha == 2:
                abastecer_alcool()
                break
            else:
                print("Escolha 1 para Gasolina ou 2 para Álcool.")

        except ValueError:
            print("Digite apenas números válidos!")

def main():
    calcular_abastecimento()

if __name__ == "__main__":
    main()
