nota1 = float(input("Digite sua nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))
media = (nota1+nota2+nota3)/3

if media>=7:
    print(f"Você foi aprovado Sua media é {media} ")
elif media>=4:
        print(f"Você esta em recuperacao Sua media é {media:.2} ")
else:
    print(f"Voce foi reprovado sua media é {media} ")


