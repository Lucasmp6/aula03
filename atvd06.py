time1 = str(input("Digite o nome do seu time " ))
time2 = str(input("Digite o nome do seu time " ))
gol1 = int(input("Digite quantos gols seu time fez " ))
gol2 = int(input("Digite quantos gols seu time fez " ))

if gol1 == gol2:
    print(f"O {time1} empatou com o {time2} ")
elif gol1>gol2:
    print(f"O {time1} fez {gol1} gols superando o {time2} ")
else:
    print(f"O {time2} superou o {time1} fazendo {gol2} gols ")