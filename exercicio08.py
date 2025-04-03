numero = int(input("Diga um numero e eu falarei se ele é par ou impar: "))
numeroEscolhido = numero%2
if numeroEscolhido == 0:
    print("Par")
else:
    print("impar")