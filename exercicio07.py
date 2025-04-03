print("Seja bem Vindo ao Posto ao Minecraft")
print(" ")
print("Aqui o cliente sempre tem vantagem")
print(" ")
gasolina = 5.80
etanol = 4.90

combustivelSelecionado = (input("Qual voce vai escolher: ")).upper()
valorSelecionado = float(input("Insira quanto vc vai pagar: "))

valorPagamentoEtanol = etanol * valorSelecionado
valorPagamentoGasolina =  gasolina * valorSelecionado

if combustivelSelecionado == "G":
    print(f"Essa é a quantidade de valor que vc terá que pagar: R${valorPagamentoGasolina}")
elif combustivelSelecionado == "E":
    print(f"Essa é a quantidade de valor que vc terá que pagar: R${valorPagamentoEtanol:.2f}")
else:
    print("Não estamos entendendo qual combustivel vc quer!")
print(" ")
print("Agradecemos a sua Preferencia")