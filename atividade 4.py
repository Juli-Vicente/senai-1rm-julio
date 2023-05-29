def contaPares(lista):
    pares = 0
    impares = 0

    for num in lista:
        if (num % 2 == 0):
            pares += 1
        else:
            impares += 1
    return pares, impares

lista = list()

q = int(input('Quantos valores haverá na lista ?'))
while q < 0:
    print('Erro')
    q = int(input('Quantos valores haverá na lista ?'))

for c in range(q):
    num = int(input('Valor:'))
    lista.append(num)

print('A quantidade de valores pares e impares são, respectivamente:',contaPares(lista))