nota1 = float(input("Digite sua nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))
media = (nota1+nota2+nota3)/3

if media<7:
    print(f"Você foi reprovado Sua media é {media:.2} ")
else:
    print(f"Você foi aprovado Sua media é {media:.2} ")

