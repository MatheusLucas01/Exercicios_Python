import math 

def calcular_area_circulo(raio: float) -> float:
    """Calcula a área de um círculo com base no raio informado."""
    return math.pi * raio**2

def raio_de_um_circulo():
    while True:
        try:
            raio = float(input("Digite o raio do círculo: "))
            area = calcular_area_circulo(raio)
            print(f"A área do círculo é de {area:.4f}")
            break
        except ValueError:
            print("Entrada Inválida! Digite apenas números. (use pontos para decimais)")

def main():
    raio_de_um_circulo()


if __name__ == "__main__":
    main()

