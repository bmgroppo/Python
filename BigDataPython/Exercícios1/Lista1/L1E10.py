#Lista 1, exercício 10

n1 = float(input('Primeiro Número: '))
op = str(input('Operação: '))
n2 = float(input('Segundo Número: '))

if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print('Caractere inválido')
    