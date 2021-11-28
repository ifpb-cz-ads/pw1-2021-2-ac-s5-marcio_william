numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Escolha qual dessas operações quer realizar -> (+,-,*,/) ")

if operacao == '+':
    print(f"O resultado da soma é de {numero1 + numero2}")
elif operacao == '-':
        print(f"O resultado da subtração é de {numero1 - numero2}")
elif operacao == '*':
        print(f"O resultado da multiplicação é de {numero1 * numero2}")
elif operacao == '/':
        print(f"O resultado da divisão é de {numero1 / numero2}")
else:
    print("Opção invalida, tente novamente")
