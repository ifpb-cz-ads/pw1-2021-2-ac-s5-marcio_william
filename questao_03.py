salario = float(input("Informe o valor so seu salario:"))
if salario >= 1250:
    aumento= salario + (salario * 10 / 100)
    print("Seu aumento foi de %.2f R$"%aumento)
else:
    aumento= salario + (salario * 15 / 100)
    print("Seu aumento foi de %.2f R$"%aumento)