while(True):
    num1 = float(input("insira o comprimento: "))
    num2 = float(input("insira a largura: "))

    def area (num1, num2):
        total = num1 * num2
        return total

    print(f"a sua media em metros é: {area(num1, num2)} m² ")
    break