# Calculadora Simples em Python

print("=" * 30)
print("        CALCULADORA SIMPLES")
print("=" * 30)
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("=" * 30)

# Entrada de dados
opcao = input("Escolha uma opção (1-4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Processamento
if opcao == "1":
    resultado = num1 + num2
    print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")
elif opcao == "2":
    resultado = num1 - num2
    print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")
elif opcao == "3":
    resultado = num1 * num2
    print(f"\n✅ Resultado: {num1} × {num2} = {resultado}")
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"\n✅ Resultado: {num1} ÷ {num2} = {resultado}")
    else:
        print("\n❌ Erro: Divisão por zero não permitida!")
else:
    print("\n❌ Opção inválida!")

print("=" * 30)