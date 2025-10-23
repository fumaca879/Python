numero1 = float(input("Digite o primeiro Número: "))
operacao = input("Digite a operação (+, -, * ou /): ")
numero2 = float(input("Digite o segundo Número: "))

from time import sleep

if operacao == "+":
    resultado = numero1 + numero2
    print(resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print(resultado)
elif operacao == "/":
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Operação invalida")
sleep(6)
