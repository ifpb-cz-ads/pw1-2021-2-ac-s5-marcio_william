kwh = float(input("Digite o consumo kw/h: "))
tipoInstalacao = input("Digite o tipo de instação -> (R,I,C): ").lower()
valor = 0
if tipoInstalacao == 'r':
    if kwh <= 500:
        valor = kwh *0.4
    else:
        valor = 0.65
elif tipoInstalacao == 'i':
    if kwh <= 1000:
        valor = kwh*0.55
    else:
        valor = kwh*0.6
elif tipoInstalacao == 'c':
    if kwh <= 5000:
        valor = kwh*0.55
    else:
        valor = kwh*0.6
else:
    print("Opção invalida, tente novamente")

print(f"O valor da conta ficou de {valor}")