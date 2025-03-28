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

