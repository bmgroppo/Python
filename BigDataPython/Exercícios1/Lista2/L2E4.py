#Lista 2, Exercício 4
a=float(input('Digite o 1º número:'))
b=float(input('Digite o 2º número:'))
c=str(input('Digite o Operador matemático:'))


if c=='+':
    print(f'A soma de {a} + {b} é: {round(a+b,2)}')
elif c=='-':
    print(f'A subtração de {a} - {b} é: {round(a-b,2)}')
elif c=='*':
    print(f'A multiplicação de {a} x {b} é: {round(a*b,2)}')
elif c=='/':
    print(f'A divisão de {a} / {b} é: {round(a/b,2)}')
else:
    print('Operação Incorreta! Use "+" "-" "*" ou "/"')

