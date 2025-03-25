<<<<<<< HEAD
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
=======
def caixa_eletronico():
    while True:
        try:
            valor_saque = int(input("Qual valor deseja sacar? "))
            if valor_saque > 600:
                print("O valor máximo é R$600")
            elif valor_saque <= 0:
                print("O valor deve ser maior que zero!")
            else:
                return valor_saque  # Retorna o valor para ser usado na função 'saque'
        except ValueError:
            print("Digite apenas números!")

def saque(valor):
    notas_disponiveis = [200, 100, 50, 20, 10, 5, 2] 
    resultado = {}

    for nota in notas_disponiveis:
        if valor >= nota:
            quantidade = valor // nota
            valor %= nota
            resultado[nota] = quantidade  # Guarda quantas notas foram usadas

    return resultado

def main():
    valor = caixa_eletronico()  # Recebe o valor do usuário
    notas = saque(valor)  # Chama a função para calcular as notas

    print("\nNotas entregues:")
    for nota, quantidade in notas.items(): # Percorre o dicionário pegando chave e valor ao mesmo tempo.
        print(f"{quantidade} nota(s) de {nota} reais")

if __name__ == "__main__":
    main()
>>>>>>> 32954e8b94df0a8292ba5e56a42116bd97366ebd
