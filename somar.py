num1 = int(input("Escolha um numero: "))
num2 = int(input("Escolha um segundo numero: "))

def somar_numeros(num1, num2):
    total = num1 + num2
    return total

def subtrair_numeros(num1, num2):
    total = num1 - num2
    return total

print("Primeira soma: ", somar_numeros(num1,num2))
print("Subtracao", subtrair_numeros(num1,num2))