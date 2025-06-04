def calculadora():
    print("=== Calculadora: Multiplicação, Divisão e Porcentagem ===")
    print("1 - Multiplicação")
    print("2 - Divisão")
    print("3 - Porcentagem (ex: quanto é X% de Y?)")
    
    operacao = input("Escolha a operação (1, 2 ou 3): ")

    if operacao not in ['1', '2', '3']:
        print("Operação inválida.")
        return

    try:
        if operacao in ['1', '2']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '1':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
            elif operacao == '2':
                if num2 == 0:
                    print("Erro: divisão por zero!")
                else:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")

        elif operacao == '3':
            percentual = float(input("Digite a porcentagem (%): "))
            total = float(input("Digite o valor total: "))
            resultado = (percentual / 100) * total
            print(f"{percentual}% de {total} = {resultado}")

    except ValueError:
        print("Erro: digite apenas números válidos.")


calculadora()
