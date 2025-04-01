nome = input(("Qual é o seu nome: "))
idade = int(input("Qual a sua idade: "))
salario = float(input("Qual o seu salario: "))
aumento = float(input("Qual foi o percentual de aumento que voce teve: "))
valorreal = salario*aumento/100
novosalario = salario+valorreal
print (f"Olá {nome} sua idade é {idade} e o seu salario atual é {salario} reais :")
print (f"seu aumento é {novosalario} ")
