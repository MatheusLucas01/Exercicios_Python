## Programa que pede as 4 notas bimestrais e calcula a média.
def calcular_media():
    while True:
        try:
            notas = [float(input(f"Digite a nota do {i+1}° bimestre: ")) for i in range (4)]
            break
        except ValueError:
            print("Digite apenas números!")

    print(f"A média final é de {sum(notas) / len(notas)}")

calcular_media()




