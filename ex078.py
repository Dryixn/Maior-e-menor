numeros = []
print('=' * 80)

for n in range(0, 5):
    num = int(input(f'Digite um número na posição {n}: '))
    numeros.append(num)

maximo = max(numeros)
minimo = min(numeros)
primeiro = numeros.index(maximo)
minprimeiro = numeros.index(minimo)

print('=' * 80)

print(f'O maior valor digitado foi {maximo} na(s) posição(ões) ', end = '')
for i in range(len(numeros)):
    if numeros[i] == maximo:
        print(f'{i} ', end = '')
print()
print(f'O menor valor digitado foi {minimo} na(s) posição(ões) ', end = '')
for i in range(len(numeros)):
    if numeros[i] == minimo:
        print(f'{i} ', end = '')
print()
print('=' * 80)
