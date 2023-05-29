from time import sleep
def contagem_regressiva (num1):
    for i in range (num1, -1, -1):
        print(i)
        sleep(0.5)
num1 = int(input("insira um numero: "))
       
print(contagem_regressiva(num1))