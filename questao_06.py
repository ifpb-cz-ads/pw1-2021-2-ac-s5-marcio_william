valor=float(input('Informe o valor da casa: '))
salario=float(input('Informe seu salario: '))
anos=int(input('Informe a quantidade de anos para pagar a casa: '))
mes=int(input('Informe a quantidade meses de complemento caso exista se nao apenas (0): '))
tempo = anos * 12 + mes
prestacao = tempo / valor
if prestacao > (salario + (salario * 30 / 100)):
    print('infelizmente é imposivel realizar emprestimo')
else:
    print('parabéns emprestimo aprovado')