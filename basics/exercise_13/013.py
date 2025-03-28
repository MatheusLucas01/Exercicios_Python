
def calcular_abastecimento():
    preco_gasolina = 2.5
    preco_alcool = 1.90

    while True:
        try:
            escolha = int(input("Escolha uma opção: 1 - Gasolina, 2 - Alcool: "))

            if escolha == 1:
                gasolina = float(input("Quantos litros de gasolina? "))
                if gasolina <= 20:
                    desconto = gasolina * preco_gasolina * 0.03
                else:
                    desconto = gasolina * preco_gasolina * 0.05
                valor_gasolina = (gasolina * preco_gasolina) - desconto
                print(f"\nValor da gasolina: R${valor_gasolina:.2f}")
                break
            elif escolha == 2:
                alcool = float(input("Quantos litros de álcool? "))
                # Calculando o desconto do álcool
                if alcool <= 20:
                    desconto = alcool * preco_alcool * 0.03  # 3% de desconto sobre o valor total
                else:
                    desconto = alcool * preco_alcool * 0.05  # 5% de desconto sobre o valor total
                valor_alcool = (alcool * preco_alcool) - desconto
                print(f"Valor do álcool com desconto: R${valor_alcool:.2f}")




            

            if gasolina < 0 or alcool < 0:
                print("Os valores devem ser positivos.")
                continue

           

            

            

            total_pagar = valor_gasolina + valor_alcool

            
            
            print(f"Desconto aplicado no álcool: R${desconto:.2f}")
            print(f"Total a pagar: R${total_pagar:.2f}")

            break  # Sai do loop ao finalizar o cálculo
        except ValueError:
            print("Digite apenas números!")

def main():
    calcular_abastecimento()

if __name__ == "__main__":
    main()