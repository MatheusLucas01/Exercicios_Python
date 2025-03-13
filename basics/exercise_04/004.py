# Exercicio Número par ou impar

print("** App impar ou par **")
while True:
    try:
        numero = int(input("Digite um número: "))
        
        if numero % 2 == 0: # Se o resto do número informado dividido por 2 = 0, o número será par
            print("Esse número é par.")
        else:
            print("Esse número é impar.")
        
        while True:
            pergunta = input("Deseja encerrar o programa? s/n: ").strip().lower()

            if pergunta == "s":
                print("Obrigado por usar nossos serviços.")
                exit() # Sai diretamente do sistema.
            elif pergunta == "n":
                print("ok continuando...")
                break
            else:
                print("Opção inválida! Digite apenas 's' ou 'n'.")

    except ValueError:
        print("Digite apenas números inteiros!")
        
