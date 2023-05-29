def numeros(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
nu1 = int(input("seu primeiro numero: "))
nu2 = int(input("seu segundo numero: "))
nu3 = int(input("seu terceiro numero: "))

resultado = numeros(nu1, nu2, nu3)

print(f"seu maior numero foi {resultado}")