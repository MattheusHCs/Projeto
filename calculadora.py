import math

def calculadora():
    print("=== Calculadora ===")
    print("Operações disponíveis: Adição, Subtração, Potenciação e Raiz Quadrada")

    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Potenciação")
        print("4 - Raiz Quadrada")
        print("5 - Sair")

        opcao = input("Digite sua opção (1/2/3/4/5): ")

        if opcao == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            if opcao == '4':
                num = float(input("Digite o número para calcular a raiz quadrada: "))
                if num < 0:
                    print("Não é possível calcular raiz quadrada de número negativo!")
                    continue
                resultado = math.sqrt(num)
                print(f"Resultado: √{num} = {resultado}")
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == '1':
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcao == '2':
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcao == '3':
                    resultado = num1 ** num2
                    print(f"Resultado: {num1} ^ {num2} = {resultado}")

        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue


calculadora()

