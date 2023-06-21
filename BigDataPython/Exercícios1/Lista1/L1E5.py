#Lista 1, exercício 5
sal = float(input('Digite o salário do funcionário: R$'))
tempo = int(input('Digite o tempo de serviço do funcionário (em anos): '))

if tempo >= 10:
    sal += (sal*0.3)
else:
    sal += (sal*0.375)
    
print(f'Novo salário com reajuste é: R${sal}')