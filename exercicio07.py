gasolina = 5.80
etanol = 4.90

combustivelSelecionado = (input("Qual voce vai escolher: ")).upper()
valorSelecionado = float(input("Insira quanto vc vai pagar: "))

valorPagamentoEtanol = etanol * valorSelecionado
valorPagamentoGasolina =  gasolina * valorSelecionado

if combustivelSelecionado == "G":
    print(valorPagamentoGasolina)
elif combustivelSelecionado == "E":
    print(valorPagamentoEtanol)

