numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 > numero2 and numero1 > numero3):
    print(f"O maior número é {numero1}")
elif (numero1 < numero2 and numero1 < numero3):
    print(f"O menor número é {numero1}")

if (numero2 > numero1 and numero2 > numero3):
    print(f"O maior número é {numero2}")
elif (numero2 < numero1 and numero2 < numero3):
    print(f"O menor número é {numero2}")

if (numero3 > numero1 and numero3 > numero2):
    print(f"O maior número é {numero3}")
elif (numero3 < numero1 and numero3 < numero2):
    print(f"O menor número é {numero3}")