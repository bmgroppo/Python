#Lista 2, Exercício 7
num=[0]*5
for i in range (5):
    num[i]=int(input(f"Digite o {i+1}º número: "))
num.sort()
print(f'Menor número: {num[0]}')
print(f'Maior número: {num[4]}')
