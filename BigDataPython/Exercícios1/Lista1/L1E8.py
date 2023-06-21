#Lista 1, exercício 8
p = float(input('Peso em kg: '))
h = float(input('Altura em m: '))
imc = p/(h**2)
c = ''

if imc < 18.5:
    c = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    c = 'Peso normal'
elif imc >= 25 and imc < 30:
    c = 'Sobrepeso'
elif imc >= 30 and imc < 35:
    c = 'Obesidade grau I'
elif imc >= 35 and imc < 40:
    c = 'Obesidade grau II'
elif imc >= 40:
    c = 'Obesidade grau III ou mórbida'
    
print(c)