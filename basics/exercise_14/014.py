print('------------------------------')
print('Calculadora de salário líquido')
print('------------------------------')

def obter_dados():
    while True:
        try:
            salario = float(input('Quanto você ganha por mês? R$ '))
            horas = float(input('Quantas horas você trabalha por mês? '))
            return salario, horas
        except ValueError:
            print("Digite um valor numérico válido!")

def calcular_inss(salario):
    if salario <= 1412.00:
        return salario * 0.075
    elif salario <= 2427.35:
        return salario * 0.09
    elif salario <= 3641.04:
        return salario * 0.12
    elif salario <= 7507.49:
        return salario * 0.14
    else:
        return 7507.49 * 0.14  # Teto

def calcular_irrf(salario_base):
    if salario_base <= 2112.00:
        return 0.0
    elif salario_base <= 2826.65:
        return salario_base * 0.075 - 158.40
    elif salario_base <= 3751.05:
        return salario_base * 0.15 - 370.40
    elif salario_base <= 4664.68:
        return salario_base * 0.225 - 651.73
    else:
        return salario_base * 0.275 - 884.96

def calcular_salario():
    salario_bruto, horas = obter_dados()
    salario_hora = salario_bruto / horas
    inss = calcular_inss(salario_bruto)
    salario_base_irrf = salario_bruto - inss
    irrf = calcular_irrf(salario_base_irrf)
    salario_liquido = salario_bruto - inss - irrf

    print('\n------ Resultado ------')
    print(f'Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'Salário por hora: R$ {salario_hora:.2f}')
    print(f'Desconto INSS: R$ {inss:.2f}')
    print(f'Desconto IRRF: R$ {irrf:.2f}')
    print(f'Salário Líquido: R$ {salario_liquido:.2f}')

def main():
    calcular_salario()

if __name__ == "__main__":
    main()
