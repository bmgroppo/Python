#Lista 1, exercício 6

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

m = (n1+n2+n3)/3
c = ''

if m >= 0 and m < 5:
    c = 'Insuficiente'
elif m >= 5 and m < 7:
    c = 'Recuperação'
elif m >= 7 and m < 9:
    c = 'Bom'
elif m >= 9:
    c = 'Muito Bom'
    
print(f'Média final: {round(m, 1)}; Conceito: {c}')    