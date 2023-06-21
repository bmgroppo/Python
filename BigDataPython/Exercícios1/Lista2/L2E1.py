#Lista 2, Exercício 1
a = float(input('Digite o 1º valor do lado do triângulo: '))
b = float(input('Digite o 2º valor do lado do triângulo: '))
c = float(input('Digite o 3º valor do lado do triângulo: '))

if (a+b) > c and a + c > b and b + c > a:
    if a==b and a==c:
        print('O triângulo é Equilátero.')
    elif a==b or a==c or b==c:
        print ('O triângulo é Isósceles.')
    else:
        print ('O triângulo é Escaleno.') 
else:
    print('Os 3 lados informados NÃO formam um triângulo')
    