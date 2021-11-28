velocidade = float(input("Qual sua velocidade: "))
if velocidade > 80:
    multa = (velocidade-80)*5
    print("Voce ultrapassou o limite de velocidade")
    print("Sua multa eh de %.2f R$"%multa)
else:
    print("velocidade permitida")