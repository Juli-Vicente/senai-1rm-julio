Salario = int(input("Qual é o seu salario atual? "))

if Salario >= 8250:
    Salario1 = Salario*1.10
    print("Seu salario com reajuste é: {}".format(Salario1))
else:
    Salario2 = Salario*1.15
    print("Seu salario com reajuste é: {}".format(Salario2))


