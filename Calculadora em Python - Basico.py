"""
Calculadora em Python
Uma calculadora simples com operações básicas
"""

import math

def adicionar(a, b):
    """Soma dois números"""
    return a + b

def subtrair(a, b):
    """Subtrai dois números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

def dividir(a, b):
    """Divide dois números"""
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def modulo(a, b):
    """Resto da divisão (mod)"""
    if b == 0:
        return "Erro: Divisão por zero!"
    return a % b

def potencia(a, b):
    """Potência a^b"""
    return math.pow(a, b)

def raiz_quadrada(a):
    """Raiz quadrada"""
    if a < 0:
        return "Erro: Raiz de número negativo!"
    return math.sqrt(a)

def percentual(a, b):
    """Percentual de a em relação a b"""
    return a * (b / 100)

def exibir_menu():
    """Exibe o menu de operações"""
    print("\n" + "="*40)
    print("         CALCULADORA PYTHON")
    print("="*40)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Módulo (resto da divisão)")
    print("\nOPERAÇÕES AVANÇADAS:")
    print("6. Potência (x²)")
    print("7. Raiz Quadrada (√)")
    print("8. Percentual (%)")
    print("\n9. Sair")
    print("="*45)

def obter_numeros():
    """Obtém dois números do usuário"""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("❌ Erro: Digite números válidos!")
        return None, None

def main():
    """Função principal - loop da calculadora"""
    print("\n🧮 Bem-vindo à Calculadora Python Avançada!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma operação (1-9): ").strip()
        
        if opcao == "9":
            print("\n👋 Obrigado por usar a calculadora. Até logo!")
            break
        
        if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("❌ Opção inválida! Digite 1-9.")
            continue
        
# Operações com 1 número
        if opcao == "7":  # Raiz quadrada
            try:
                num = float(input("Digite o número: "))
                resultado = raiz_quadrada(num)
                operacao = "√"
                print(f"\n✅ Resultado: {operacao}{num} = {resultado}")
            except ValueError:
                print("❌ Erro: Digite um número válido!")
            continue

        # Operações que precisam de 2 números
        num1, num2 = obter_numeros()
        if num1 is None:
            continue
        
        # Processar operações com 2 números
        if opcao == "1":
            resultado = adicionar(num1, num2)
            operacao = "+"
        elif opcao == "2":
            resultado = subtrair(num1, num2)
            operacao = "-"
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            operacao = "*"
        elif opcao == "4":
            resultado = dividir(num1, num2)
            operacao = "/"
        elif opcao == "5":
            resultado = modulo(num1, num2)
            operacao = "mod"
        elif opcao == "6":
            resultado = potencia(num1, num2)
            operacao = "^"
        elif opcao == "8":
            resultado = percentual(num1, num2)
            operacao = f"{num2}% de"
        
        print(f"\n✅ Resultado: {num1} {operacao} {num2} = {resultado}")

if __name__ == "__main__":
    main()