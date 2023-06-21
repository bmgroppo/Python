#Lista 1, exercício 9

n = int(input('número do ano: '))

m = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

if n < 1 or n > 12:
    print('Número Inválido')
else:
    print(m[n-1])