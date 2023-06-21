#Lista 2, Exercício 2
s = float(input('Digite o salário: '))

if s<=600:
    print('Você está isento de desconto.')
elif s>600 and s<=1200:
    print(f'Seu desconto de INSS é de: R${round(s*0.2,2)}')
elif s>1200 and s<=2000:
    print(f'Seu desconto de INSS é de: R${round(s*0.25,2)}')
else:
    print(f'Seu desconto de INSS é de: R${round(s*0.3,2)}')