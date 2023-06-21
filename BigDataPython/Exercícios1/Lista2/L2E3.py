#Lista 2, Exercício 3
n=float(input('Digite a nota do aluno de (1-10):'))
c =''

if n<=1:
    c='F'
elif n>1 and n<=2:
    c='E'
elif n>2 and n<=4:
    c='D'
elif n>4 and n<=6:
    c='C'
elif n>6 and n<=8:
    c='B'
elif n>8 and n<=10:
    c='A'
else:
    c='Incorreta'

print(f'A nota do aluno é: {c}')